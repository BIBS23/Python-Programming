c = 1
while(c>0):
    msg = input('enter the message in lowercase')
    dist = int(input('enter the distance'))
    new = ""
    choice = int(input('enter choice'))
    if(choice == 1):
        
        for i in msg:
            ordvalue = ord(i)
            cypher = ordvalue+dist
            if(cypher>ord('z')):
                cypher = (ord(i)+dist-97)%26+97
            new+=chr(cypher)
        print(new)
        
