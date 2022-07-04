"""
This function returns the nth fibonacci number
iteratively.
"""

def fibonacci_itr(n):
    previous = 0
    current = 1

    for i in range(n-1):
        current_old = current
        current = current + previous
        previous = current_old
    return print(current)

fibonacci_itr(8)