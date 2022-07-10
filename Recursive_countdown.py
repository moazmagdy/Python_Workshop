"""
This function creates a countdown  that recursively counts down from
integer n until it hits 0.
"""

def countdown(n):
    if n == 0:
        #Terminal case
        return print(n)
    else:
        print(n)
        #Recursive case
        return countdown(n-1)