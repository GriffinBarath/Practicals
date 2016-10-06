from Prac08.taxiClass import Taxi


class SilverServiceTaxi(Taxi):
    """specialised version of a car that includes fanciness and increasing fares based on fanciness"""

    def __init__(self, name, fuel, fanciness):
        """initialises a SilverServiceTaxi instance, based on parent Taxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness
        self.flagfall = 4.50

    def __str__(self):
        """returns a string representation like a taxi but with fanciness"""
        return "{} plus a flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """get the current price for the taxi trip"""
        return self.price_per_km * self.current_fare_distance + self.flagfall


if __name__ == '__main__':
    hummer = SilverServiceTaxi('Hummer', 200, 2)
    print(hummer.__str__())
    hummer.start_fare()
    hummer.drive(10)
    fare = hummer.get_fare()
    print(fare)
