"""
This simple program uses a function called fibonacci to find
the outcome of any give number in a fibonacci series
"""

#Fibonacci Series 
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <=1:
        return n
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    return memo[n]

number = int(input("Enter any number: "))
if number < 0:
    print("Pls eneter a postive number")
else:
    result = fibonacci(number)
    print(f"The fibo of {number} is: {result}")