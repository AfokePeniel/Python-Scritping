logo = """
 _____________________
|  _________________  |
| | Calculator   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator = {
       "+" : add,
       "-" : subtract,
       "*" : multiply,
       "/" : divide

    }

def selection():
    print(logo)
    first_numb = float(input("What's the first number?: \t"))
    should_continue = True
    
    while should_continue:
        for key in calculator:
            print(key)
        
        pick_operator = input("Pick an operation: \t")
        second_numb = float(input("What's the second number?: \t"))
        
        if pick_operator in calculator:
            calculation_function = calculator[pick_operator]
            result = calculation_function(first_numb, second_numb)
            print(f"{first_numb} {pick_operator} {second_numb} = {result}")
            
            continue_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'x' to exit: \t").lower()
            
            if continue_cal == 'y':
                first_numb = result
            elif continue_cal == 'n':
                should_continue = False
                print("\n" * 20)
                selection()
            elif continue_cal == 'x':
                print("Goodbye!")
                should_continue = False
selection()