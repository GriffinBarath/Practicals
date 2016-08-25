def main():
    name = input("Please enter your name:")
    while len(name) < 1:
        name = input("Please enter your name:")
    for letter in name[::2]:
        print(letter)

main()