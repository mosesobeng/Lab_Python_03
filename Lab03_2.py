##Lab03_2a

emptyString =''
for i in range(1,7):
    for j in range(1,i+1):
        emptyString+=str(j)
    emptyString+="\n"
print emptyString

##Lab03_2b

emptyString =''
for i in range(6,-1,-1):
    for j in range(1,i+1):
        emptyString+=str(j)
    emptyString+="\n"
print emptyString


##Lab03_2c
emptyString =''
for i in range(1,8):
    for j in range(6,0,-1):
        if(j>i-1):
            emptyString+=" "
        else:   
            emptyString+=str(j)
    emptyString+="\n"
print emptyString


##Lab03_2d
emptyString =''
for i in range(6,0,-1):
    for j in range(1,8):
        if(j<i-1):
            emptyString+=" "
        else:   
            emptyString+=str(j)
    emptyString+="\n"
print emptyString

