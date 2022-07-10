"""
This function finds nth Fibonacci numbers
using dynamic programming approach using explicit memoization.
"""
stored_results = {}

def fibonacci_dyn(n):
    #Check if n is already computed and memoized in {stored_results}
    if n in stored_results:
        return stored_results[n]
    
    if n == 0 or n ==1:
        stored_results[n] = n
        return stored_results[n]
    else:
    #Memoization of new values
        stored_results[n] = fibonacci_dyn(n-2) + fibonacci_dyn(n-1)
        return stored_results[n]
