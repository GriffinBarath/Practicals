from random import randint
from Prac08.taxiClass import Car


class UnreliableCar(Car):
    """docstring lol"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliabilityTest = randint(0, 100)
        print(reliabilityTest)
        if self.reliability < reliabilityTest:
            distance_driven = 0
        elif distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven

        return distance_driven

mitsy = UnreliableCar("Mitsy", 100, 75)
print(mitsy.drive(40))
print(mitsy.__str__())
