file = open("testcode.asm","r")
myfile = (file.readline())
print(myfile)

LC = 0
while file.readline():
    myfile = file.readline()
    print(myfile)
    if(myfile.find("ORG")):
        for i in myfile:
            if i.isnumeric():
                LC = int(i)
        print(LC)