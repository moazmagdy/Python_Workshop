"""
This function creates the factorial of a number number N 
using recursion.
"""
import time

start = time.perf_counter()

def factorial_recursive(n):
    if n == 1:
        #Terminal case
        return 1
    else:
        #Recursive case
        return n * factorial_recursive(n-1)

print(time.perf_counter() - start)

factorial_recursive(5)