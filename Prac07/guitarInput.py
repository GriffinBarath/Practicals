from Prac07.guitarClass import Guitar

def main():
    guitars = []
    print("My guitars!")
    name = "1"
    #while len(name) >0:
    #    name = input("Name:")
    #    year = input("Year:")
    #    cost = input("Cost: $")
    #    guitars.append(Guitar(name, year, cost))
    #    print(guitars)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    i = 1
    for guitar in guitars:
        isVintage = guitar.isVintage()
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, isVintage))
        i += 1


main()
