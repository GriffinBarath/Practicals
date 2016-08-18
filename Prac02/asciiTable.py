MIN_NUMBER = 33
MAX_NUMBER = 127

character = input("Enter a character:")
print("The ASCII code for " + character + " is " + str(ord(character)))
number = int(input("Enter a number between 33 and 127:"))
while number > MAX_NUMBER or number < MIN_NUMBER:
    number = int(input("Invalid number! Please enter a number between 33 and 127:"))
print("The character for "+str(number)+" is "+str(chr(number)))
asciiCount = MIN_NUMBER
for num in range(MIN_NUMBER, MAX_NUMBER):
    print("{:<5s}{:>5s}".format(str(asciiCount), str(chr(asciiCount))))
    asciiCount += 1
