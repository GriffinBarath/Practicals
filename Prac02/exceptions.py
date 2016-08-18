"""
Questions
1. When will a ValueError occur?
When the numerator or denominator is entered as a float not an integer.
2. When will a ZeroDivisionError occur?
When the denominator is entered as 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, add a simple while loop, which request an entry until the entry =>0.
"""

try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:
 print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
 print("Cannot divide by zero!")
print("Finished.")

