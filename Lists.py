
"""
List Definition: A list is a mutable data structure in Python used to store an ordered collection of items, which can be of different types.

Key List Operations:

Initialization: to_do_list = [] creates an empty list.
Adding Items: Use .append(item) to add items to the end of the list.
Looping: Use a for loop to iterate over the list's elements.
Modifying Items: The .remove(item) method removes a specified item from the list.
Use Case in the Code:

The list acts as a dynamic container for managing tasks in the to-do list, allowing addition, iteration, and removal of tasks.

"""

to_do_list = []

to_do_list.append("Eat")
to_do_list.append("Pray")
to_do_list.append("Sleep")

print("My to-do list for the festivities: ")

for task in to_do_list:
    print("-", task.lower())

print("Then after my festivities:")
to_do_list.remove("Eat")

for task in to_do_list:
    print("-", task)