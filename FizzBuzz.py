"""
This a program that automatically prints the solution to a list of auto generated numbers 
from 1 - 100 and prints according to these conditions

- if the number is divisible by 3 then instead of printing the number it should print "Fizz"
- if the number is divisible by 5 then instead of printing the number it should print "Buzz"
- if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
"""

#FuzzBuzz Game
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
