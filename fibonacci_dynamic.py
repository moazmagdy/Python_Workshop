"""
This function finds nth Fibonacci numbers
using dynamic programming approach.
"""
stored_results = {0: 0, 1:1}

def fibonacci_dyn(n):
    if n in stored_results:
        return stored_results[n]
    else:
        stored_results[n] = fibonacci_dyn(n-2) + fibonacci_dyn(n-1)
        return stored_results[n]
