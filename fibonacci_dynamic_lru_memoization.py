"""
This function finds nth Fibonacci numbers
using dynamic programming approach using LRU decorator memoization.
"""
from functools import lru_cache

@lru_cache(maxsize= 1000)
def fibonacci_dyn(n):

    if n == 0 or n ==1:
        return n
    else:
        return fibonacci_dyn(n-2) + fibonacci_dyn(n-1)
