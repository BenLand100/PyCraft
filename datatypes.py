from struct import pack,unpack

def w_char(data):
    return pack('>c',data)

def r_char(sio):
    return unpack('>c',sio.read(1))[0]

def w_byte(data):
    return pack('>b',data)

def r_byte(sio):
    return unpack('>b',sio.read(1))[0]

def w_ubyte(data):
    return pack('>B',data)

def r_ubyte(sio):
    return unpack('>B',sio.read(1))[0]

def w_short(data):
    return pack('>h',data)

def r_short(sio):
    return unpack('>h',sio.read(2))[0]

def w_shortchar(data):
    return pack('>H',ord(data))

def r_shortchar(sio):
    return chr(unpack('>H',sio.read(2))[0])

def w_int(data):
    return pack('>i',data)

def r_int(sio):
    return unpack('>i',sio.read(4))[0]

def w_long(data):
    return pack('>q',data)

def r_long(sio):
    return unpack('>q',sio.read(8))[0]

def w_float(data):
    return pack('>f',data)

def r_float(sio):
    return unpack('>f',sio.read(4))[0]

def w_double(data):
    return pack('>d',data)

def r_double(sio):
    return unpack('>d',sio.read(8))[0]

def w_string8(data):
    return w_short(len(data))+data

def r_string8(sio):
    length = parse_short(sio)
    return sio.read(length)

def w_string16(data):
    chars = ''.join([w_shortchar(i) for i in data])
    return w_short(len(data))+chars

def r_string16(sio):
    length = r_short(sio)
    result = ''
    for i in range(length):
        result += r_shortchar(sio)
    return result
    

def w_bool(data):
    if data:
        return '\x01'
    else:
        return '\x00'

def r_bool(sio):
    data = sio.read(1)
    if data == '\x01':
        return True
    else:
        return False
