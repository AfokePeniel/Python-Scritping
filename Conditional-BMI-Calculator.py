"""
This is a simple program that askes a user for their height and weight
And the calculate, and determines the person's BMI in various conditions

"""


#Conditional BMI Clculator

weight = float(input("Enter your height in cm: \t"))
height = int(input("Enter your weight in kg: \t"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi:.2f}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi:.2f}, You are normal weight")
elif bmi > 30:
    print(f"Your bmi is {bmi:.2f}, You are slightly overweight")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    