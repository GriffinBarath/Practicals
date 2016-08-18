"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
__author__ ='Griffin Barath'

sales = 1
while sales > 0:
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        modifier= 0.1
    else:
        modifier= 0.15
    bonus = sales * modifier
    if sales < 0:
        print()
    else:
        print("Bonus: "+str(bonus))
