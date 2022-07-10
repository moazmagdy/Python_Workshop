"""
This function returns the nth fibonacci number
recursively.
"""
def fibonacci_recur(n):

    if n == 0 or n == 1:
        #Terminal case
        return n
    else:
        #Recursive case
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)