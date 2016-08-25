def main():
    months = int(input("How many months?"))
    monthlyIncomes = list()
    for month in range(1, months+1):
        incomeInput = int(input("Enter income for month "+ str(month)+":"))
        monthlyIncomes.append(incomeInput)
    print(monthlyIncomes)

main()