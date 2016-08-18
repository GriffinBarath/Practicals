__author__ ='Griffin Barath'

numberOfItems= int(input("Please enter the number of items to ship: "))
while numberOfItems < 0:
    print("Invalid Entry")
    numberOfItems= int(input("Please enter the number of items to ship: "))
itemNumber= 1
customerItems=list()
for items in range(numberOfItems):
    itemEntry= int(input("Please enter the cost of item "+str(itemNumber)+": "))
    customerItems.append(itemEntry)
    itemNumber = itemNumber + 1
totalCost= sum(customerItems)
print("Number of Items: "+str(numberOfItems))
for entry in customerItems:
    print("Price of Item: "+str(entry))
print("Total cost for "+str(numberOfItems)+" items is $"+str(totalCost))


