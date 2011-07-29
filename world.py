#all the stuff about blocks/chunks/world structure

import zlib
from cStringIO import StringIO
from math import floor
from datatypes import *
from visual import *

def chunkPos(x,y,z):
    cx = int(floor(x))>>4
    cy = int(floor(y))>>7
    cz = int(floor(z))>>4
    return cx,cy,cz
    
def localPos(x,y,z):
    lx = int(floor(x))&15
    ly = int(floor(y))&127
    lz = int(floor(z))&15
    return lx,ly,lz
        
class Block(object):
    def __init__(self,x,y,z,type=0):
        self.x,self.y,self.z = x,y,z
        self.type = type
        #self._box = None
    def setType(self,type):
        self.type = type
        #self._box = box(pos=(self.x,self.y,self.z),length=1,width=1,height=1,color=color.red) if (type == 3) else None 
    
class Chunk(object):
    def __init__(self,cx,cy,cz,):
        self.cx,self.cy,self.cz = (cx,cy,cz)
        print cx,cy,cz
        self._blocks = [[[Block((cx<<4)+lx,(cy<<7)+ly,(cz<<4)+lz) for lz in range(16)] for ly in range(128)] for lx in range(16)]
    def getBlock(self,lx,ly,lz):
        return self._blocks[lx][ly][lz]
    def update(self,lx,ly,lz,sx,sy,sz,data):
        data = StringIO(zlib.decompress(data))
        for x in range(lx,sx+1):
            for z in range(lz,sz+1):
                for y in range(ly,sy+1):
                    self._blocks[x][y][z].setType(r_ubyte(data))
        #ignore the rest for now
        data.close()
        
class World(object):
    def __init__(self):
        self._chunks = {}
    def updateChunk(self,x,y,z,sx,sy,sz,data):
        cx,cy,cz = chunkPos(x,y,z)
        chunk = None
        if (cx,cy,cz) in self._chunks:
            chunk = self._chunks[(cx,cy,cz)]
        else:
            chunk = Chunk(cx,cy,cz)
            self._chunks[(cx,cy,cz)] = chunk
        lx,ly,lz = localPos(x,y,z)
        chunk.update(lx,ly,lz,sz,sy,sz,data)
    def getChunk(self,x,y,z):
        cx,cy,cz = chunkPos(x,y,z)
        return self._chunks[(cx,cy,cz)] if (cx,cy,cz) in self._chunks else None
    def getBlock(self,x,y,z):
        chunk = self.getChunk(x,y,z)
        lx,ly,lz = localPos(x,y,z)
        return chunk.getBlock(lx,ly,lz) if chunk else None
