class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.price_per_km = 1.2
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class SilverServiceTaxi(Taxi):
    """specialised version of a car that includes fanciness and increasing fares based on fanciness"""

    def __init__(self, name, fuel, fanciness):
        """initialises a SilverServiceTaxi instance, based on parent Taxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * self.price_per_km
        self.flagfall = 4.50

    def __str__(self):
        """returns a string representation like a taxi but with fanciness"""
        print("{} plus a flagfall of ${:.2f}".format(super().__str__(), self.flagfall))

    def get_fare(self):
        """get the current price for the taxi trip"""
        return self.price_per_km * self.current_fare_distance + self.flagfall


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets drive!")
    loopCondition = True
    totalFare = 0
    while loopCondition == True:
        menuChoice = str(input("q)uit, c)hoose taxi, d)rive"))
        menuChoice.lower()
        while menuChoice != "q" and menuChoice != "c" and menuChoice != "d":
            menuChoice = str(input("Invalid Response!\nq)uit, c)hoose taxi, d)rive"))
        if menuChoice == "c":
            currentTaxi = chooseTaxi(taxis)
        elif menuChoice == "d":
            try:
                totalFare = driveTaxi(currentTaxi, totalFare)
            except:
                UnboundLocalError
                print("Please choose a taxi first!")
        elif menuChoice == "q":
            loopCondition = False




def chooseTaxi(taxiList):
    taxiCounter = 0
    for choice in taxiList:
        print("{} - {}".format(taxiCounter, choice.__str__()))
        #print(choice.__str__())
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
