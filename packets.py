from datatypes import *
from cStringIO import StringIO

###Packet 0x00
def r_keep_alive(data):
	return {'id':0x00}
def w_keep_alive():
	return w_byte(0x00)

###Packet 0x01
def r_login_request_cts(data):
	return {'id':0x01,'Version':r_int(data),'Username':r_string16(data),'MapSeed':r_long(data),'Dimension':r_byte(data)}
def w_login_request_cts(Version,Username,MapSeed,Dimension):
	return w_byte(0x01)+w_int(Version)+w_string16(Username)+w_long(MapSeed)+w_byte(Dimension)

###Packet 0x01
def r_login_request_stc(data):
	return {'id':0x01,'EntityID':r_int(data),'Unknown':r_string16(data),'MapSeed':r_long(data),'Dimension':r_byte(data)}
def w_login_request_stc(EntityID,Unknown,MapSeed,Dimension):
	return w_byte(0x01)+w_int(EntityID)+w_string16(Unknown)+w_long(MapSeed)+w_byte(Dimension)

###Packet 0x02
def r_handshake_cts(data):
	return {'id':0x02,'Username':r_string16(data)}
def w_handshake_cts(Username):
	return w_byte(0x02)+w_string16(Username)

###Packet 0x02
def r_handshake_stc(data):
	return {'id':0x02,'ConnectionHash':r_string16(data)}
def w_handshake_stc(ConnectionHash):
	return w_byte(0x02)+w_string16(ConnectionHash)

###Packet 0x03
def r_chat_message(data):
	return {'id':0x03,'Message':r_string16(data)}
def w_chat_message(Message):
	return w_byte(0x03)+w_string16(Message)

###Packet 0x04
def r_time_update(data):
	return {'id':0x04,'Time':r_long(data)}
def w_time_update(Time):
	return w_byte(0x04)+w_long(Time)

###Packet 0x05
def r_entity_equipment(data):
	return {'id':0x05,'EntityID':r_int(data),'Slot':r_short(data),'ItemID':r_short(data),'Damage':r_short(data)}
def w_entity_equipment(EntityID,Slot,ItemID,Damage):
	return w_byte(0x05)+w_int(EntityID)+w_short(Slot)+w_short(ItemID)+w_short(Damage)

###Packet 0x06
def r_spawn_position(data):
	return {'id':0x06,'X':r_int(data),'Y':r_int(data),'Z':r_int(data)}
def w_spawn_position(X,Y,Z):
	return w_byte(0x06)+w_int(X)+w_int(Y)+w_int(Z)

###Packet 0x07
def r_use_entity(data):
	return {'id':0x07,'EntityID':r_int(data)}
def w_use_entity(EntityID):
	return w_byte(0x07)+w_int(EntityID)

###Packet 0x08
def r_update_health(data):
	return {'id':0x08,'Health':r_short(data)}
def w_update_health(Health):
	return w_byte(0x08)+w_short(Health)

###Packet 0x09
def r_respawn(data):
	return {'id':0x09,'World':r_byte(data)}
def w_respawn(World):
	return w_byte(0x09)+w_byte(World)

###Packet 0x0A
def r_player(data):
	return {'id':0x0A,'OnGround':r_bool(data)}
def w_player(OnGround):
	return w_byte(0x0A)+w_bool(OnGround)

###Packet 0x0B
def r_player_position(data):
	return {'id':0x0B,'X':r_double(data),'Y':r_double(data),'Stance':r_double(data),'Z':r_double(data),'OnGround':r_bool(data)}
def w_player_position(X,Y,Stance,Z,OnGround):
	return w_byte(0x0B)+w_double(X)+w_double(Y)+w_double(Stance)+w_double(Z)+w_bool(OnGround)

###Packet 0x0C
def r_player_look(data):
	return {'id':0x0C,'Yaw':r_float(data),'Pitch':r_float(data),'OnGround':r_bool(data)}
def w_player_look(Yaw,Pitch,OnGround):
	return w_byte(0x0C)+w_float(Yaw)+w_float(Pitch)+w_bool(OnGround)

###Packet 0x0D
def r_player_position_and_look_cts(data):
	return {'id':0x0D,'X':r_double(data),'Y':r_double(data),'Stance':r_double(data),'Z':r_double(data),'Yaw':r_float(data),'Pitch':r_float(data),'OnGround':r_bool(data)}
def w_player_position_and_look_cts(X,Y,Stance,Z,Yaw,Pitch,OnGround):
	return w_byte(0x0D)+w_double(X)+w_double(Y)+w_double(Stance)+w_double(Z)+w_float(Yaw)+w_float(Pitch)+w_bool(OnGround)

###Packet 0x0D
def r_player_position_and_look_stc(data):
	return {'id':0x0D,'X':r_double(data),'Stance':r_double(data),'Y':r_double(data),'Z':r_double(data),'Yaw':r_float(data),'Pitch':r_float(data),'OnGround':r_bool(data)}
def w_player_position_and_look_stc(X,Stance,Y,Z,Yaw,Pitch,OnGround):
	return w_byte(0x0D)+w_double(X)+w_double(Stance)+w_double(Y)+w_double(Z)+w_float(Yaw)+w_float(Pitch)+w_bool(OnGround)

###Packet 0x0E
def r_player_digging(data):
	return {'id':0x0E,'Status':r_byte(data),'X':r_int(data),'Y':r_byte(data),'Z':r_int(data),'Face':r_byte(data)}
def w_player_digging(Status,X,Y,Z,Face):
	return w_byte(0x0E)+w_byte(Status)+w_int(X)+w_byte(Y)+w_int(Z)+w_byte(Face)

###Packet 0x0F
def r_player_block_placement(data):
	packet = {'id':0x0F,'X':r_int(data),'Y':r_byte(data),'Z':r_int(data),'Direction':r_byte(data),'BlockID':r_short(data)}
	if packet['BlockID'] >= 0: packet.update({'Amount':r_byte(data),'Damage':r_short(data)})
	return packet
def w_player_block_placement(X,Y,Z,Direction,BlockID,Amount,Damage):
	data = w_byte(0x0F)+w_int(X)+w_byte(Y)+w_int(Z)+w_byte(Direction)+w_short(BlockID)
	if BlockID >= 0: data += w_byte(Amount)+w_short(Damage)
	return data

###Packet 0x10
def r_holding_change(data):
	return {'id':0x10,'SlotID':r_short(data)}
def w_holding_change(SlotID):
	return w_byte(0x10)+w_short(SlotID)

###Packet 0x11
def r_use_bed(data):
	return {'id':0x11,'EntityID':r_int(data),'InBed':r_byte(data),'X':r_int(data),'Y':r_byte(data),'Z':r_int(data)}
def w_use_bed(EntityID,InBed,X,Y,Z):
	return w_byte(0x11)+w_int(EntityID)+w_byte(InBed)+w_int(X)+w_byte(Y)+w_int(Z)

###Packet 0x12
def r_animate(data):
	return {'id':0x12,'EntityID':r_int(data),'Animate':r_byte(data)}
def w_animate(EntityID,Animate):
	return w_byte(0x12)+w_int(EntityID)+w_byte(Animate)

###Packet 0x13
def r_act(data):
	return {'id':0x13,'EntityID':r_int(data),'Action':r_byte(data)}
def w_act(EntityID,Action):
	return w_byte(0x13)+w_int(EntityID)+w_byte(Action)

###Packet 0x14
def r_spawn_player(data):
	return {'id':0x14,'EID':r_int(data),'Name':r_string16(data),'X':r_int(data),'Y':r_int(data),'Z':r_int(data),'Yaw':r_byte(data),'Pitch':r_byte(data),'CurrentItem':r_short(data)}
def w_spawn_player(EID,Name,X,Y,Z,Yaw,Pitch,CurrentItem):
	return w_byte(0x14)+w_int(EID)+w_string16(Name)+w_int(X)+w_int(Y)+w_int(Z)+w_byte(Yaw)+w_byte(Pitch)+w_short(CurrentItem)

###Packet 0x15
def r_pickup_spawn(data):
	return {'id':0x15,'EntityID':r_int(data),'Item':r_short(data),'Count':r_byte(data),'Damage':r_short(data),'X':r_int(data),'Y':r_int(data),'Z':r_int(data),'Yaw':r_byte(data),'Pitch':r_byte(data),'Roll':r_byte(data)}
def w_pickup_spawn(EntityID,Item,Count,Damage,X,Y,Z,Yaw,Pitch,Roll):
	return w_byte(0x15)+w_int(EntityID)+w_short(Item)+w_byte(Count)+w_short(Damage)+w_int(X)+w_int(Y)+w_int(Z)+w_byte(Yaw)+w_byte(Pitch)+w_byte(Roll)

###Packet 0x16
def r_collect_item(data):
	return {'id':0x16,'CollectedEID':r_int(data),'CollectorEID':r_int(data)}
def w_collect_item(CollectedEID,CollectorEID):
	return w_byte(0x16)+w_int(CollectedEID)+w_int(CollectorEID)

###Packet 0x17
def r_add_object(data):
	packet = {'id':0x17,'EntityID':r_int(data),'Type':r_byte(data),'X':r_int(data),'Y':r_int(data),'Z':r_int(data),'Flag':r_int(data)}
	if packet['Flag'] > 0: packet.update({'Xmap':r_short(data),'Ymap':r_short(data),'Zmap':r_short(data)})
	return packet
def w_add_object(EntityID,Type,X,Y,Z,Flag,Xmap,Ymap,Zmap):
	return w_byte(0x17)+w_int(EntityID)+w_byte(Type)+w_int(X)+w_int(Y)+w_int(Z)+w_int(Flag)+w_short(Xmap)+w_short(Ymap)+w_short(Zmap)

###Packet 0x18
def r_spawn_mob(data):
	return {'id':0x18,'EntityID':r_int(data),'Type':r_byte(data),'X':r_int(data),'Y':r_int(data),'Z':r_int(data),'Yaw':r_byte(data),'Pitch':r_byte(data),'Metadata':r_metadata(data)}
def w_spawn_mob(EntityID,Type,X,Y,Z,Yaw,Pitch,Metadata):
	return w_byte(0x18)+w_int(EntityID)+w_byte(Type)+w_int(X)+w_int(Y)+w_int(Z)+w_byte(Yaw)+w_byte(Pitch)+w_metadata(Metadata)

###Packet 0x19
def r_painting(data):
	return {'id':0x19,'EntityID':r_int(data),'Title':r_String16(data),'X':r_int(data),'Y':r_int(data),'Z':r_int(data),'Direction':r_int(data)}
def w_painting(EntityID,Title,X,Y,Z,Direction):
	return w_byte(0x19)+w_int(EntityID)+w_String16(Title)+w_int(X)+w_int(Y)+w_int(Z)+w_int(Direction)

###Packet 0x1B
def r_stance_update(data):
	return {'id':0x1B,'A':r_float(data),'B':r_float(data),'C':r_float(data),'D':r_float(data),'E':r_boolean(data),'F':r_boolean(data)}
def w_stance_update(A,B,C,D,E,F):
	return w_byte(0x1B)+w_float(A)+w_float(B)+w_float(C)+w_float(D)+w_boolean(E)+w_boolean(F)

###Packet 0x1C
def r_entity_velocity(data):
	return {'id':0x1C,'EntityID':r_int(data),'vX':r_short(data),'vY':r_short(data),'vZ':r_short(data)}
def w_entity_velocity(EntityID,vX,vY,vZ):
	return w_byte(0x1C)+w_int(EntityID)+w_short(vX)+w_short(vY)+w_short(vZ)

###Packet 0x1D
def r_destroy_entity(data):
	return {'id':0x1D,'EntityID':r_int(data)}
def w_destroy_entity(EntityID):
	return w_byte(0x1D)+w_int(EntityID)

###Packet 0x1E
def r_entity(data):
	return {'id':0x1E,'EntityID':r_int(data)}
def w_entity(EntityID):
	return w_byte(0x1E)+w_int(EntityID)

###Packet 0x1F
def r_entity_relative_move(data):
	return {'id':0x1F,'EntityID':r_int(data),'dX':r_byte(data),'dY':r_byte(data),'dZ':r_byte(data)}
def w_entity_relative_move(EntityID,dX,dY,dZ):
	return w_byte(0x1F)+w_int(EntityID)+w_byte(dX)+w_byte(dY)+w_byte(dZ)

###Packet 0x20
def r_entity_look(data):
	return {'id':0x20,'EntityID':r_int(data),'Yaw':r_byte(data),'Pitch':r_byte(data)}
def w_entity_look(EntityID,Yaw,Pitch):
	return w_byte(0x20)+w_int(EntityID)+w_byte(Yaw)+w_byte(Pitch)

###Packet 0x21
def r_entity_look_and_relative_move(data):
	return {'id':0x21,'EntityID':r_int(data),'dX':r_byte(data),'dY':r_byte(data),'dZ':r_byte(data),'Yaw':r_byte(data),'Pitch':r_byte(data)}
def w_entity_look_and_relative_move(EntityID,dX,dY,dZ,Yaw,Pitch):
	return w_byte(0x21)+w_int(EntityID)+w_byte(dX)+w_byte(dY)+w_byte(dZ)+w_byte(Yaw)+w_byte(Pitch)

###Packet 0x22
def r_entity_teleport(data):
	return {'id':0x22,'EntityID':r_int(data),'X':r_int(data),'Y':r_int(data),'Z':r_int(data),'Yaw':r_byte(data),'Pitch':r_byte(data)}
def w_entity_teleport(EntityID,X,Y,Z,Yaw,Pitch):
	return w_byte(0x22)+w_int(EntityID)+w_int(X)+w_int(Y)+w_int(Z)+w_byte(Yaw)+w_byte(Pitch)

###Packet 0x26
def r_entity_status(data):
	return {'id':0x26,'EntityID':r_int(data),'Status':r_byte(data)}
def w_entity_status(EntityID,Status):
	return w_byte(0x26)+w_int(EntityID)+w_byte(Status)

###Packet 0x27
def r_attach_entity(data):
	return {'id':0x27,'EntityID':r_int(data)}
def w_attach_entity(EntityID):
	return w_byte(0x27)+w_int(EntityID)

###Packet 0x28
def r_entity_metadata(data):
	return {'id':0x28,'EntityID':r_int(data),'Metadata':r_metadata(data)}
def w_entity_metadata(EntityID,Metadata):
	return w_byte(0x28)+w_int(EntityID)+w_metadata(Metadata)

###Packet 0x32
def r_prechunk(data):
	return {'id':0x32,'X':r_int(data),'Z':r_int(data),'Mode':r_bool(data)}
def w_prechunk(X,Z,Mode):
	return w_byte(0x32)+w_int(X)+w_int(Z)+w_bool(Mode)
	
###Packet 0x33
def r_map_chunk(data):
	packet = {'id':0x33,'X':r_int(data),'Y':r_short(data),'Z':r_int(data),'SizeX':r_byte(data),'SizeY':r_byte(data),'SizeZ':r_byte(data),'CompressedSize':r_int(data)}
	packet['CompressedData'] = data.read(packet['CompressedSize'])
	if len(packet['CompressedData']) != packet['CompressedSize']: raise struct.error('Not enough data')
	return packet
def w_map_chunk(X,Y,Z,SizeX,SizeY,SizeZ,CompressedSize,CompressedData):
	return w_byte(0x33)+w_int(X)+w_short(Y)+w_int(Z)+w_byte(SizeX)+w_byte(SizeY)+w_byte(SizeZ)+w_int(CompressedSize)+CompressedData

'''
###Packet 0x34
def r_multi_block_change(data):
	return {'id':0x34,'ChunkX':r_int(data),'ChunkZ':r_int(data),'ArraySize':r_short(data),'CoordinateArray':r_short array(data),'TypeArray':r_byte array(data),'MetadataArray':r_byte array(data)}
def w_multi_block_change(ChunkX,ChunkZ,ArraySize,CoordinateArray,TypeArray,MetadataArray):
	return w_byte(0x34)+w_int(ChunkX)+w_int(ChunkZ)+w_short(ArraySize)+w_short array(CoordinateArray)+w_byte array(TypeArray)+w_byte array(MetadataArray)
'''

###Packet 0x35
def r_block_change(data):
	return {'id':0x35,'X':r_int(data),'Y':r_byte(data),'Z':r_int(data),'Type':r_byte(data),'Metadata':r_byte(data)}
def w_block_change(X,Y,Z,Type,Metadata):
	return w_byte(0x35)+w_int(X)+w_byte(Y)+w_int(Z)+w_byte(Type)+w_byte(Metadata)

###Packet 0x36
def r_block_action(data):
	return {'id':0x36,'X':r_int(data),'Y':r_short(data),'Z':r_int(data),'DataA ':r_byte(data),'DataB':r_byte(data)}
def w_block_action(X,Y,Z,DataA ,DataB):
	return w_byte(0x36)+w_int(X)+w_short(Y)+w_int(Z)+w_byte(DataA )+w_byte(DataB)

'''
###Packet 0x3C
def r_explosion(data):
	return {'id':0x3C,'X':r_double(data),'Y':r_double(data),'Z':r_double(data),'Unknown':r_float(data),'RecordCount':r_int(data),'Records':r_{(byte, byte, byte) * count}(data)}
def w_explosion(X,Y,Z,Unknown,RecordCount,Records):
	return w_byte(0x3C)+w_double(X)+w_double(Y)+w_double(Z)+w_float(Unknown)+w_int(RecordCount)+w_(byte, byte, byte) * count(Records)
'''

###Packet 0x3D
def r_sound_effect(data):
	return {'id':0x3D,'EffectID':r_int(data),'X':r_int(data),'Y':r_byte(data),'Z':r_int(data),'SoundData':r_int(data)}
def w_sound_effect(EffectID,X,Y,Z,SoundData):
	return w_byte(0x3D)+w_int(EffectID)+w_int(X)+w_byte(Y)+w_int(Z)+w_int(SoundData)

###Packet 0x46
def r_new_state(data):
	return {'id':0x46,'Reason':r_byte(data)}
def w_new_state(Reason):
	return w_byte(0x46)+w_byte(Reason)

###Packet 0x47
def r_thunderbolt(data):
	return {'id':0x47,'EntityID':r_int(data),'Unknown':r_boolean(data),'X':r_int(data),'Y':r_int(data),'Z':r_int(data)}
def w_thunderbolt(EntityID,Unknown,X,Y,Z):
	return w_byte(0x47)+w_int(EntityID)+w_boolean(Unknown)+w_int(X)+w_int(Y)+w_int(Z)

###Packet 0x64
def r_open_window(data):
	return {'id':0x64,'WindowId':r_byte(data),'InventoryType':r_byte(data),'WindowTitle':r_string8(data),'NumberOfSlots':r_byte(data)}
def w_open_window(WindowId,InventoryType,WindowTitle,NumberOfSlots):
	return w_byte(0x64)+w_byte(WindowId)+w_byte(InventoryType)+w_string8(WindowTitle)+w_byte(NumberOfSlots)

###Packet 0x65
def r_close_window(data):
	return {'id':0x65,'WindowID':r_byte(data)}
def w_close_window(WindowID):
	return w_byte(0x65)+w_byte(WindowID)

###Packet 0x66
def r_window_click(data):
	return {'id':0x66,'WindowID':r_byte(data),'Slot':r_short(data),'RightClick':r_byte(data),'ActionNumber':r_short(data),'Shift':r_bool(data),'ItemID':r_short(data),'ItemCount':r_byte(data),'ItemUses':r_short(data)}
def w_window_click(WindowID,Slot,RightClick,ActionNumber,Shift,ItemID,ItemCount,ItemUses):
	return w_byte(0x66)+w_byte(WindowID)+w_short(Slot)+w_byte(RightClick)+w_short(ActionNumber)+w_bool(Shift)+w_short(ItemID)+w_byte(ItemCount)+w_short(ItemUses)

###Packet 0x67
def r_set_slot(data):
	packet = {'id':0x67,'WindowID':r_byte(data),'Slot':r_short(data),'ItemID':r_short(data)}
	if packet['ItemID'] != -1:
	    packet.update({'ItemCount':r_byte(data),'ItemUses':r_short(data)})
	return packet
def w_set_slot(WindowID,Slot,ItemID,ItemCount=0,ItemUses=0):
    data = w_byte(0x67)+w_byte(WindowID)+w_short(Slot)+w_short(ItemID)
    if ItemID != -1:
        data += w_byte(ItemCount)+w_short(ItemUses)
    return data

###Packet 0x68
def r_window_items(data):
	packet = {'id':0x68,'WindowID':r_byte(data),'Count':r_short(data)}
	payload = []
	for i in range(packet['Count']):
	    id = r_short(data)
	    if id != -1:
	        payload.append((id,r_byte(data),r_short(data)))
	    else:
	        payload.append(None)
	packet['Payload'] = payload
	return packet
def w_window_items(WindowID,Count,Payload):
	data = w_byte(0x68)+w_byte(WindowID)+w_short(Count)
	for item in Payload:
	    if item:
	        data += w_short(item[0])+w_byte(item[1])+w_short(item[2])
	    else:
	        data += w_short(-1)


###Packet 0x69
def r_update_progress_bar(data):
	return {'id':0x69,'WindowID':r_byte(data),'ProgressBar':r_short(data),'Value':r_short(data)}
def w_update_progress_bar(WindowID,ProgressBar,Value):
	return w_byte(0x69)+w_byte(WindowID)+w_short(ProgressBar)+w_short(Value)

###Packet 0x6A
def r_transaction(data):
	return {'id':0x6A,'WindowID':r_byte(data),'ActionNumber':r_short(data),'Accepted':r_boolean(data)}
def w_transaction(WindowID,ActionNumber,Accepted):
	return w_byte(0x6A)+w_byte(WindowID)+w_short(ActionNumber)+w_boolean(Accepted)

###Packet 0x82
def r_update_sign(data):
	return {'id':0x82,'X':r_int(data),'Y':r_short(data),'Z':r_int(data),'Text1':r_string16(data),'Text2':r_string16(data),'Text3':r_string16(data),'Text4':r_string16(data)}
def w_update_sign(X,Y,Z,Text1,Text2,Text3,Text4):
	return w_byte(0x82)+w_int(X)+w_short(Y)+w_int(Z)+w_string16(Text1)+w_string16(Text2)+w_string16(Text3)+w_string16(Text4)

'''
###Packet 0x83
def r_map_data(data):
	return {'id':0x83,'UnknownA':r_short(data),'UnknownB':r_short(data),'TextLength':r_ubyte(data),'Text':r_byte array(data)}
def w_map_data(UnknownA,UnknownB,TextLength,Text):
	return w_byte(0x83)+w_short(UnknownA)+w_short(UnknownB)+w_unsigned byte(TextLength)+w_byte array(Text)
'''

###Packet 0xC8
def r_increment_statistic(data):
	return {'id':0xC8,'StatisticID':r_int(data),'Amount':r_byte(data)}
def w_increment_statistic(StatisticID,Amount):
	return w_byte(0xC8)+w_int(StatisticID)+w_byte(Amount)

###Packet 0xFF
def r_kick(data):
	return {'id':0xFF,'Message':r_string16(data)}
def w_kick(Message):
	return w_byte(0xFF)+w_string16(Message)

packet_readers = {
	0x00:r_keep_alive,
	0x01:r_login_request_stc,
	0x02:r_handshake_stc,
	0x03:r_chat_message,
	0x04:r_time_update,
	0x05:r_entity_equipment,
	0x06:r_spawn_position,
	0x07:r_use_entity,
	0x08:r_update_health,
	0x09:r_respawn,
	0x0A:r_player,
	0x0B:r_player_position,
	0x0C:r_player_look,
	0x0D:r_player_position_and_look_stc,
	0x0E:r_player_digging,
	0x0F:r_player_block_placement,
	0x10:r_holding_change,
	0x11:r_use_bed,
	0x12:r_animate,
	0x13:r_act,
	0x14:r_spawn_player,
	0x15:r_pickup_spawn,
	0x16:r_collect_item,
	0x17:r_add_object,
	0x18:r_spawn_mob,
	0x19:r_painting,
	0x1B:r_stance_update,
	0x1C:r_entity_velocity,
	0x1D:r_destroy_entity,
	0x1E:r_entity,
	0x1F:r_entity_relative_move,
	0x20:r_entity_look,
	0x21:r_entity_look_and_relative_move,
	0x22:r_entity_teleport,
	0x26:r_entity_status,
	0x27:r_attach_entity,
	0x28:r_entity_metadata,
	0x32:r_prechunk,
	0x33:r_map_chunk,
	#0x34:r_multi_block_change,
	0x35:r_block_change,
	0x36:r_block_action,
	#0x3C:r_explosion,
	0x3D:r_sound_effect,
	0x46:r_new_state,
	0x47:r_thunderbolt,
	0x64:r_open_window,
	0x65:r_close_window,
	0x66:r_window_click,
	0x67:r_set_slot,
	0x68:r_window_items,
	0x69:r_update_progress_bar,
	0x6A:r_transaction,
	0x82:r_update_sign,
	#0x83:r_map_data,
	0xC8:r_increment_statistic,
	0xFF:r_kick
}

def readpacket(databuf):
    sio = StringIO(databuf)
    pid = r_ubyte(sio)
    if pid in packet_readers:
        return (packet_readers[pid](sio),databuf[sio.tell():])
    else: raise Exception('Unknown Packet: ' + hex(pid))

