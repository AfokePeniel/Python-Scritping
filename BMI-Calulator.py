"""
Create a program that calculates a person's Body Mass Index (BMI).
It asks for the user's weight and height repsectively.
Covert the height to float datatype and Covert the weight to int data type respectively.
But the final answer for the person's BMI should be rounded up to 2 decimal places.

""" 

#BMI Calculator

greetings = "Welcome to the BMI Calculator"
print(greetings)

height = input("Enter your height in meters:  \t")
weight = input("Enter your weight in kilograms: \t")

new_height = float(height)
new_weight = int(weight)

bmi = round(new_weight / (new_height ** 2),2)
print(f"Your BMI is : {bmi}\t")