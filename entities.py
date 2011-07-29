#everything about entities/players/mobs/etc

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
