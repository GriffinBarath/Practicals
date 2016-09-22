from Prac08.taxiClass import Taxi
from Prac08.silverServiceTaxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets drive!")
    loopCondition = True
    totalFare = 0
    while loopCondition:
        menuChoice = str(input("q)uit, c)hoose taxi, d)rive"))
        menuChoice.lower()
        while menuChoice != "q" and menuChoice != "c" and menuChoice != "d":
            menuChoice = str(input("Invalid Response!\nq)uit, c)hoose taxi, d)rive"))
        if menuChoice == "c":
            currentTaxi = chooseTaxi(taxis)
        elif menuChoice == "d":
            # noinspection PyBroadException
            try:
                totalFare = driveTaxi(currentTaxi, totalFare)
            except:
                UnboundLocalError
                print("Please choose a taxi first!")
        elif menuChoice == "q":
            loopCondition = False
    print("Total trip cost ${:.2f}\nTaxis are now:".format(totalFare))
    for taxi in taxis:
        print(taxi)



def chooseTaxi(taxiList):
    taxiCounter = 0
    for taxi in taxiList:
        print("{} - {}".format(taxiCounter, taxi))
        #print(taxi.__str__())
        taxiCounter += 1
    taxiChoice = int(input("Choose Taxi:"))
    while taxiChoice not in range(0, taxiCounter):
        taxiChoice = int(input("Invalid Taxi number, please enter a valid number."))
    currentTaxi = taxiList[taxiChoice]
    return currentTaxi


def driveTaxi(currentTaxi, totalFare):
    fare = 0
    distance = int(input("Drive how far?"))
    currentTaxi.start_fare
    currentTaxi.drive(distance)
    fare = currentTaxi.get_fare()
    totalFare = totalFare + fare
    print("Your {} trip cost you ${:.2f}".format(currentTaxi.name, fare))
    print("Bill to date: {:.2f}".format(totalFare))
    return totalFare


main()
