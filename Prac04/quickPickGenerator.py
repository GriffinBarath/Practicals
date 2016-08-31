import random


def main():
    counter = int(input("How many Quick Picks:"))
    while counter < 1:
        counter = input("Please enter a number greater than 0 to play!\nHow many Quick Picks?")
    quickPicks = [1, 2, 3, 4, 5, 6, ]
    for pick in range(counter):
        for number in quickPicks:
            for i in range(6):
                quickPicks[i] = random.randint(1, 45)
            quickPicks.sort()
            print(number, end=" ")
        print("")


main()
