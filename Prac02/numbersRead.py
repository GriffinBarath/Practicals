numbersFile = open("numbers.txt", 'r')
numberOne = numbersFile.readline().strip()
numberTwo = numbersFile.readline().strip()
numbersTotal = int(numberOne)+int(numberTwo)
print(numbersTotal)
numbersFile.close()
