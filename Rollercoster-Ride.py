height = int(input("Kindly enter your height in cm: "))
bill = 0

if height >= 120:
    print("Hurray, you can ride!")
    age = int(input("Kindly enter your age: "))
    if age <=12:
        bill = 5
        print("Child tickets are $5")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12") 
    picture = (input("Do you want a photo while rollercoasting? Enter 'Y' or 'y' for Yes and 'N' or 'n' for No: "))
    if picture == 'Y' :
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("Sorry you can't ride, you have to grow taller!")