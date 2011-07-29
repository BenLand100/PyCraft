#all the stuff about blocks/chunks/world structure

from math import floor

class Block(object):
    def __init__(self):
        pass
    
class Chunk(object):
    def __init__(self):
        self._blocks = [[[Block() for z in range(16)] for y in range(128)] for x in range(16)]
    def getBlock(self,lx,ly,lz):
        return self._blocks[lx][ly][lz]
    def update(self,lx,ly,lz,sx,sy,sz,data):
        pass
    
class World(object):
    def __init__(self):
        self._chunks = {}
    def chunkPos(self,x,y,z):
        cx = int(floor(x)) >> 4
        cy = int(floor(y)) >> 7
        cz = int(floor(z)) >> 4
        return cx,cy,cz
    def localPos(self,x,y,z):
        cx,cy,cz = self.chunkPos(x,y,z)
        lx = int(floor(x-16*cx))
        ly = int(floor(y-16*cy))
        lz = int(floor(z-16*cz))
        return lx,ly,lz
    def updateChunk(self,x,y,z,sx,sy,sz,data):
        cx,cy,cz = self.chunkPos(x,y,z)
        chunk = None
        if (cx,cy,cz) in self._chunks:
            chunk = self._chunks[(cx,cy,cz)]
        else:
            chunk = Chunk()
            self._chunks[(cx,cy,cz)] = chunk
        lx,ly,lz = self.localPos(x,y,z)
        chunk.update(lx,ly,lz,sz,sy,sz,data)
    def getChunk(self,x,y,z):
        cx,cy,cz = self.chunkPos(x,y,z)
        return (self._chunks[(cx,cy,cz)],cx,cy,cz) if (cx,cy,cz) in self._chunks else None
    def getBlock(self,x,y,z):
        chunk = self.getChunk(x,y,z)
        lx,ly,lz = self.localPos(x,y,z)
        return chunk.getBlock(lx,ly,lz) if chunk else None
