"""
Create a Simple program that greets a user.
The program asks for the city the user grew up in and also the user's pet name in new lines respectively.
Next it combines both input together to form a Band name.
"""

#Band Generator Program

greetings = "Welcome to Band Name Generator"
print(greetings)

city_name = input("Enter the name of city you grew up in \n")
pet_name = input("Enter the name of your pet \n")

band_name = (city_name + "" + pet_name)
print(f"Your Band name is {band_name} !")

