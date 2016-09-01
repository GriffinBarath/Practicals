import random


def main():
    MIN_NUMBER = 1
    MAX_NUMBER = 45
    NUMBERS_IN_PICK = 6
    number_of_picks = int(input("How many Quick Picks:"))
    while number_of_picks < 1:
        number_of_picks = input("Please enter a number greater than 0 to play!\nHow many Quick Picks?")
    for pick in range(number_of_picks):
        quickPicks = []
        for i in range(NUMBERS_IN_PICK):
            randomNumber = random.randint(MIN_NUMBER, MAX_NUMBER)
            while randomNumber in quickPicks:
                randomNumber = random.randint(MIN_NUMBER, MAX_NUMBER)
            quickPicks.append(randomNumber)
        quickPicks.sort()
        print(quickPicks, end=" ")
        print("")


main()
