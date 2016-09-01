import random


def main():
    MIN_NUMBER = 1
    MAX_NUMBER = 45
    NUMBERS_IN_PICK = 6
    counter = int(input("How many Quick Picks:"))
    while counter < 1:
        counter = input("Please enter a number greater than 0 to play!\nHow many Quick Picks?")
    quickPicks = [1, 2, 3, 4, 5, 6, ]
    for pick in range(counter):
        for number in quickPicks:
            for i in range(NUMBERS_IN_PICK):
                quickPicks[i] = random.randint(MIN_NUMBER, MAX_NUMBER)
            quickPicks.sort()
            print(number, end=" ")
        print("")


main()
