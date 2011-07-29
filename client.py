#!/usr/bin/python

#Everything for managing the client state

import socket,struct,time

from packets import *
from world import *
from entities import *

class Client(object):
    def __init__(self):
        self._socket = socket.socket()
        self.us = Player()
        self.world = World()
        self.inworld = False
        self.tick = 0;
        #physics
        self.lasttime = time.time()
        self.deltat = 0.05
        self.gravity = 9.8
        self.onground = False
        
    def connect(self,host='127.0.0.1',port=25565):
        self.host = host
        self.port = port
        try:
            self._socket.connect((self.host,self.port))
        except socket.error, msg:
            print msg
            return False
        self._socket.setblocking(0);
        return True
        
    def login(self,username):
        self.us.name = username
        self.send(w_handshake_cts(username))
        
    def sendPos(self):
        self.send(w_player_position_and_look_cts(self.us.x,self.us.y,self.us.y+self.us.height,self.us.z,self.us.yaw,self.us.pitch,self.onground))
        print self.us.x,self.us.y,self.us.z
    
    def send(self,packet):
        self._socket.send(packet)
    
    def _keepalive(self,packet):
        print 'KeepAlive'
        self.send(w_keep_alive())
       
    def _login(self,packet):
        self.us.eid = packet['EntityID']
        print 'Login Success'
     
    def _handshake(self,packet):
        self.send(w_login_request_cts(14,self.us.name,0,0))
        
    def _chat(self,packet):
        print 'CHAT',packet['Message']
        
    def _playeronground(self,packet):
        self.us.onground = packet['OnGround']
        print 'Echoing position', packet
        self.sendPos()
    
    def _playerpos(self,packet):
        self._playeronground(packet)
        self.us.x = packet['X']
        self.us.y = packet['Y']
        self.us.z = packet['Z']
        self.us.height = packet['Stance'] - self.us.y
        self.onground = packet['OnGround']
        print 'Echoing position', packet
        self.sendPos()
        
    def _playerlook(self,packet):
        self._playeronground(packet)
        self.us.yaw = packet['Yaw']
        self.us.pitch = packet['Pitch']
        self.onground = packet['OnGround']
        print 'Echoing position', packet
        self.sendPos()
    
    def _playerlookandpos(self,packet):
        self.us.yaw = packet['Yaw']
        self.us.pitch = packet['Pitch']
        self.us.x = packet['X']
        self.us.y = packet['Y']
        self.us.z = packet['Z']
        self.onground = packet['OnGround']
        self.us.height = packet['Stance'] - self.us.y
        print 'Echoing position', self.us.height, packet['Stance'],self.us.y
        self.sendPos()
        self.inworld = True
        
    def _chunkdata(self,packet):
        print 'Chunk Update'
        self.world.updateChunk(packet['X'],packet['Y'],packet['Z'],packet['SizeX'],packet['SizeY'],packet['SizeZ'],packet['CompressedData'])
        
    def _kicked(self,packet):
        print 'KICKED:',packet['Message']
        
    def _ignore(self,packet):
        pass
    
    def _dump(self,packet):
        print hex(packet['id']),packet
        
    hooks = {
        0x00:_keepalive,0x01:_login,0x02:_handshake,0x03:_chat,
        
        0x0A:_playeronground,0x0B:_playerpos,0x0C:_playerlook,0x0D:_playerlookandpos, #player location
    
        0x18:_ignore,0x1c:_ignore,0x1d:_ignore,0x1e:_ignore,0x1f:_ignore,0x20:_ignore,0x21:_ignore,0x22:_ignore, #entity moving stuff
        0x32:_ignore,0x33:_chunkdata, #chunk stuff
        
        0xff:_kicked
    };
    _data = '';

    def pump(self):
        #read packets
        try:
            read = self._socket.recv(16)
            if len(read) == 0: 
                return False
            self._data += read
            packet,self._data = readpacket(self._data)
            if packet['id'] in self.hooks:
                self.hooks[packet['id']](self,packet)
            else:
                print 'Unhandled: ' + hex(packet['id'])
        except socket.error,msg:
            pass
        except struct.error,msg:
            pass
        #do physics
        if self.inworld and time.time() - self.lasttime > self.deltat:
            elapsed = time.time() - self.lasttime 
            print elapsed
            self.lasttime = time.time()
            block = self.world.getBlock(self.us.x,self.us.y,self.us.z)
            if block:
                print 'block:',block.type
                if block.type > 0:
                    self.onground = True
                    self.us.vy = 0
                    self.us.y = round(self.us.y)
                else:
                    self.onground = False
                    self.us.vy -= self.gravity*elapsed
            else:
                print 'Our chunk is not loaded!'
            self.us.x += self.us.vx*elapsed
            self.us.y += self.us.vy*elapsed
            self.us.z += self.us.vz*elapsed
            self.sendPos()
        return True
            
            
client = Client();
if client.connect():
    client.login('YourMom')
    while client.pump(): pass
    print 'Disconnected'
else:
    print 'Failed to Connect'
