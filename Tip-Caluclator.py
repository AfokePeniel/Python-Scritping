"""
Create a program that calculates a Bill.
With a tip selected and it should be splited amongs an inputed number of persons equally.

"""

greetings = "Welcome to Foxy's Eat House!"
print(greetings)

bill = float(input("Kindly enter your bill amount: \t$"))
tip_percent = int(input("Select a tip percentage 10, 12, or 15: \t"))
number_of_persons = int(input("Kindly enter the number of persons to slipt the bill amount: \t"))
tip_amt = (bill * tip_percent) / 100
total_bill = (bill + tip_amt ) / number_of_persons 

print(f"Your Total bill splited equally with tip is: ${total_bill:.2f}") 