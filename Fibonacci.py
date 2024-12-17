"""
This simple program uses a function called fibonacci to find
the outcome of 10 in a fibonacci series
"""

#Fibonacci Series 
def fibonacci(n):
    if n<=1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)
print("The fibonacci at position 10 is:", fibonacci(10))