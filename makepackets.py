#!/usr/bin/python

from re import *
from string import *

f = open('packetdump', 'r')

packets = []

lastname = ''
while True:
    line = f.readline()
    if line == '': 
        break
    m = search('===([^=\(]*)',line)
    if m: lastname = strip(m.group(1))
    if search('wikitable',line) != None:
        f.readline()
        if search('Packet ID',f.readline()): #foundone
            while not search('row1',f.readline()): pass
            id = ''
            fields = []
            while True:
                line = f.readline()
                if not search('class=',line): break
                if search('col0',line):
                    m = search('0x(..)',line)
                    if m: 
                        id = m.group(1)
                        line = f.readline()  
                    else:
                        m1 = search('" \\| (.*)',line)
                        m2 = search('" \\| (.*)',f.readline())
                        if m1 and m2 and not search("Total Size",m1.group(1)): fields.append((m1.group(1),m2.group(1))) 
                if search('col1',line):
                    m1 = search('" \\| (.*)',line)
                    m2 = search('" \\| (.*)',f.readline())
                    if m1 and m2: fields.append((m1.group(1),m2.group(1))) 
            packets.append((replace(lower(lastname),' ','_'), id, fields))
               
file = ''
 
for lastname,id,fields in packets:
    code = '###Packet 0x'+id+'\n'
    code += 'def r_'+lastname+'(data):\n\treturn {\'id\':0x'+id+','
    code += ','.join(['\''+name+'\':r_'+type+'(data)' for (name,type) in fields])
    code += '}\n'
    code += 'def w_'+lastname+'('+','.join([name for (name,type) in fields])+'):\n\treturn w_byte(0x'+id+')+'
    code += '+'.join(['w_'+type+'('+name+')' for (name,type) in fields])
    code += '\n\n'
    file += code

file+='packet_readers = {'+','.join(['\n\t0x'+id+':r_'+lastname+'' for (lastname,id,fields) in packets])+'\n}'

print file
    

        
f.close()
