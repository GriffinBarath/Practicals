from datetime import date
class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return"{} ({}) : ${:.2f}".format(name, year, cost, )

    def getAge(self):
        return date.today().year - self.year

    def isVintage(self):
        if self.getAge() > 49:
            return"(vintage)"
        else:
            return""

