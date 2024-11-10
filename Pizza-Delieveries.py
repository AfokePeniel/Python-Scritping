"""
This program is an example of what's used when ordering pizza from a store
A user makes his or her choice of Pizza before proceeding to pay
based on the choice of pizza with toppings of with pepperoni or extra cheese.

"""

#Pizza Delieveries
greetings = "Welcome to Python Pizza Deliveries!"
print(greetings)

small_pizza = 0
medium_pizza = 0
large_pizza = 0
amt_extra_cheese = 1
amt_LM_pepperoni = 3

size = input("What size of Pizza do you want? Type 'S' for Small, 'M' for Medium, 'L' for Large: ")
if size == 's':
    small_pizza = 15
    amt_pepperoni = 2
    print(f"Small size pizza is ${small_pizza} .")
    pepperoni = input("Add Pepperoni on your Pizza for additional $2? Type 'Y' for Yes and 'N' for No: ")
    extra_cheese = input("Add extra Cheese for $1? Type 'Y' for Yes and 'N' for No: ")
    if pepperoni == 'y' and extra_cheese == 'y':
        total_small = small_pizza + amt_pepperoni + amt_extra_cheese
        print(f"Your total price for Pizza with Pepperoni and extra Cheese is :${total_small} .")
    elif pepperoni == 'n' and extra_cheese == 'y':
        total_small = small_pizza + amt_extra_cheese 
        print(f"Your total price for Pizza with extra Cheese is :${total_small} .")
    elif pepperoni == 'y' and extra_cheese == 'n':
        total_small = small_pizza + amt_pepperoni 
        print(f"Your total price for Pizza with Pepperoni is :${total_small}")
    else:
        print(f"Your total price for Pizza with no Pepperoni or extra Cheese is :${small_pizza} .")
elif size == 'm':
    medium_pizza = 20
    print(f"Medium size pizza is ${medium_pizza} .")
    pepperoni = input("Add Pepperoni on your Pizza for additional $3? Type 'Y' for Yes and 'N' for No: ")
    extra_cheese = input("Add extra Cheese for $1? Type 'Y' for Yes and 'N' for No: ")
    if pepperoni == 'y' and extra_cheese == 'y':
        total_medium = medium_pizza + amt_LM_pepperoni + amt_extra_cheese
        print(f"Your total price for Pizza with Pepperoni and extra Cheese is :${total_medium} .")
    elif pepperoni == 'n' and extra_cheese == 'y':
        total_medium = medium_pizza + amt_extra_cheese 
        print(f"Your total price for Pizza with extra Chesse is :${total_medium} .")
    elif pepperoni == 'y' and extra_cheese == 'n':
        total_medium = medium_pizza + amt_LM_pepperoni 
        print(f"Your total price for Pizza with Pepperoni is :${total_medium} .")
    else:
        print(f"Your total price for Pizza with no Pepperoni or extra Cheese is :${medium_pizza} .")
elif size == "l":
    large_pizza = 25
    print(f"Large size pizza is ${large_pizza}")
    pepperoni = input("Add Pepperoni on your Pizza for additional $2? Type 'Y' for Yes and 'N' for No: ")
    extra_cheese = input("Add extra Cheese for $1? Type 'Y' for Yes and 'N' for No: ")
    if pepperoni == 'y' and extra_cheese == 'y':
        total_large = large_pizza + amt_LM_pepperoni + amt_extra_cheese
        print(f"Your total price for Pizza with Pepperoni and extra Cheese is :${total_large} .")
    elif pepperoni == 'n' and extra_cheese == 'y':
        total_large = large_pizza + amt_extra_cheese 
        print(f"Your total price for Pizza with extra Chesse is :${total_large} .")
    elif pepperoni == 'y' and extra_cheese == 'n':
        total_large = large_pizza + amt_LM_pepperoni 
        print(f"Your total price for Pizza with Pepperoni is :${total_large} .")
    else:
        print(f"Your total price for Pizza is :${large_pizza}")
else:
    print("You entered a wrong option, pls try again.")
