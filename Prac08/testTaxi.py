"""
CP1404/CP5632 Practical
Car class
"""
from Prac08.taxiClass import Taxi

taxiOne = Taxi('Prius 1', 100)
taxiOne.start_fare()
taxiOne.drive(40)
fare = taxiOne.get_fare()
print(fare)
taxiOne.start_fare()
taxiOne.drive(100)
fare = taxiOne.get_fare()
print(fare)
print(taxiOne.__str__())
