"""
This function creates the factorial of a number number N 
using iterations.
"""
import time

def factorial_iter(n):
    start = time.perf_counter()
    factorial = n
    for i in reversed(range(1, n)):
        factorial *= i
    elapsed_time = time.perf_counter() - start
    return "Elapsed time is {}".format(elapsed_time),factorial