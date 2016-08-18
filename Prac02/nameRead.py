nameFileIn = open("name.txt", 'r')
name = nameFileIn.read().strip()
print("Your name is "+name)
nameFileIn.close()
