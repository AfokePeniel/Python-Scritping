"""
This is a program that takes a users input and determines
if it's a leap year or not

"""

#Leap Year Calculator

year = int(input("Kindly enter a year: \t"))


if year % 400 == 0:
    print("This is a leap year")
elif year % 100 == 0:
    print("This is not a leap year")
elif year % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
   
   