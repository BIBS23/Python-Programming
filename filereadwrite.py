s = 'programming in python'
f1 = open("code","w")
f1.write(s)
print('file writed')
f1.close()
f2 = open("code","r")
content = f2.read()
print("your content is :",content)
f2.close()
