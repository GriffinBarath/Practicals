def main():
    numbers = []
    for i in range(5):
        number = int(input("Please input a number:"))
        numbers.append(number)
    print("The first number is ", numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is ", min(numbers))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))
main()