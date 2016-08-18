nameFileOut = open("name.txt", 'w')
name = str(input("Please enter your name:"))
print(name, file=nameFileOut)
nameFileOut.close()
