def main():
    MIN_NUMBER = 33
    MAX_NUMBER = 127

    character = input("Enter a character:")
    print("The ASCII code for " + character + " is " + str(ord(character)))
    number = getNumber(MIN_NUMBER, MAX_NUMBER)
    print("The character for " + str(number) + " is " + str(chr(number)))
    asciiCount = MIN_NUMBER
    for num in range(MIN_NUMBER, MAX_NUMBER):
        print("{:<5s}{:>5s}".format(str(asciiCount), str(chr(asciiCount))))
        asciiCount += 1


def getNumber(lower, upper):
    validInput = False
    while not validInput:
        try:
            num = int(input("Enter a number:"))
            if num < lower or num > upper:
                validInput = False
                print("Please enter a valid number!")
            else:
                validInput = True
        except ValueError:
            print("Please enter a valid number!")
    return num

main()
