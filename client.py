#!/usr/bin/python

import socket,struct
import time
from packets import *

class Entity(object):
    def __init__(self,eid=0,x=0,y=0,z=0,pitch=0,yaw=0,vx=0,vy=0,vz=0):
        self.eid = eid
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw
        self.vx = vx
        self.vy = vy
        self.vz = vz
    
class Player(Entity):
    def __init__(self,eid=0,name='',x=0,y=0,z=0,pitch=0,yaw=0,vx=0,vy=0,vz=0):
        Entity.__init__(self,eid,x,y,z,pitch,yaw,vx,vy,vz)
        self.name = name
    
class Mob(Entity):
    def __init__(self,eid=0,mobtype=0,metadata=[],x=0,y=0,z=0,pitch=0,yaw=0,vx=0,vy=0,vz=0):
        Entity.__init__(self,eid,x,y,z,pitch,yaw,vx,vy,vz)
        self.mobtype = mobtype
        self.metadata = metadata

class Client(object):
    def __init__(self):
        self._socket = socket.socket()
        self.us = Player()
        
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
        self.send(w_player_position_and_look_cts(self.us.x,self.us.y,self.us.stance,self.us.z,self.us.yaw,self.us.pitch,self.us.onground))
    
    def send(self,packet):
        self._socket.send(packet)
    
    def _keepalive(self,packet):
        print 'KeepAlive'
        self.send(w_keepalive())
       
    def _login(self,packet):
        self.us.eid = packet['EntityID']
        print 'Party == Started'
     
    def _handshake(self,packet):
        self.send(w_login_request_cts(14,self.us.name,0,0))
        
    def _playeronground(self,packet):
        self.us.onground = packet['OnGround']
        print 'Echoing position', packet
        self.sendPos()
    
    def _playerpos(self,packet):
        self._playeronground(packet)
        self.us.x = packet['X']
        self.us.y = packet['Y']
        self.us.z = packet['Z']
        self.us.stance = packet['Stance']
        self.us.onground = packet['OnGround']
        print 'Echoing position', packet
        self.sendPos()
        
    def _playerlook(self,packet):
        self._playeronground(packet)
        self.us.yaw = packet['Yaw']
        self.us.pitch = packet['Pitch']
        self.us.onground = packet['OnGround']
        print 'Echoing position', packet
        self.sendPos()
    
    def _playerlookandpos(self,packet):
        self.us.yaw = packet['Yaw']
        self.us.pitch = packet['Pitch']
        self.us.x = packet['X']
        self.us.y = packet['Y']
        self.us.z = packet['Z']
        self.us.onground = packet['OnGround']
        self.us.stance = packet['Stance']
        print 'Echoing position', packet
        self.sendPos()
        
    def _kicked(self,packet):
        print 'KICKED:',packet['Message']
        
    def _ignore(self,packet):
        pass
    
    def _dump(self,packet):
        print hex(packet['id']),packet
        
    hooks = {
        0x00:_keepalive,0x01:_login,0x02:_handshake,
        
        0x0A:_playeronground,0x0B:_playerpos,0x0C:_playerlook,0x0D:_playerlookandpos, #player location
    
        0x18:_ignore,0x1c:_ignore,0x1d:_ignore,0x1e:_ignore,0x1f:_ignore,0x20:_ignore,0x21:_ignore, #entity moving stuff
        0x32:_dump,0x33:_dump, #chunk stuff
        
        0xff:_kicked
    };
    _data = '';

    def pump(self):
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
        return True
            
            
client = Client();
if client.connect():
    client.login('YourMom')
    while client.pump(): pass
    print 'Disconnected'
else:
    print 'Failed to Connect'
