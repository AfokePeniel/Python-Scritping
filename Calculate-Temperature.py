"""
This is a program that calculates temperature.
It askes the user to input details for temperature conversion.
From Celsius to Fahrenheit and Fahrenheit to Celsius.
And rounded up to a whole number

"""

#Calculate Temperature

celsius = int(input("Enter a value for celcius: ")) 
fahrenheit = int(input("Enter a value for fahrenheit: "))
cel_to_fah = round((fahrenheit- 32) * 5/9)
fah_to_cel = round((celsius * 9/5) + 32)

print(f"Your temperature in Celsius is: {fah_to_cel}""°C")
print(f"Your temperature in Fahrenheit is: {cel_to_fah}""°F")
