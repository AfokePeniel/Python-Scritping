"""
This is a program checks if a user's input
is an Odd or Even number
and prints out a statment respectively.

"""


#Odd and Even Number check

numb = int(input("Kindly enter any number: "))

if numb % 2 == 0:
    print(f"Your input as {numb} is an Even number")
elif numb % 2 != 0:
    print(f"Your input as {numb} is an Odd number")