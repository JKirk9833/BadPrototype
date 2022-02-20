#!/usr/bin/python

with open(".\gladiusMODDED\gladius_bec\data\config\lookuptext_eng.txt","r",encoding="utf8") as f:
    lines = f.readlines()

linesBin = []
numLines = len(lines)
fileSize = 13+(numLines*4)
addressesEndOffset = fileSize-1

with open(".\gladiusMODDED\gladius_bec\data\config\lookuptext_eng.bin","wb") as f:
    f.write((numLines+1).to_bytes(2, byteorder="little"))
    f.write(b'\x00\x00')
    
    i = 0
    while i < numLines:
        mid=lines[i]
        mid = mid[0:len(mid)-1]
        mid = mid[len(str(i+1))+1:len(mid)]
        lines[i]=mid
        lines[i] = lines[i].replace(r"\r\n","\n")    
        fileSize = fileSize+len(lines[i])+1
        i += 1
    
    f.write(fileSize.to_bytes(3, byteorder="little"))
    f.write(b'\x00')
    
    f.write(addressesEndOffset.to_bytes(3, byteorder="little"))
    f.write(b'\x00')
    
    i = 0
    offset = addressesEndOffset+1
    while i < numLines:
        f.write(offset.to_bytes(3, byteorder="little"))
        f.write(b'\x00')
        offset += len(lines[i])+1
        #print(offset)
        i += 1
    f.write(b'\x00')
    
    i = 0
    while i < numLines:
        f.write(lines[i].encode("ansi"))
        f.write(b'\x00')
        i += 1