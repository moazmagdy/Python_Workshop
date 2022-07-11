""""
This script uses the nonlocal keyword to define the scope of a variable within a function.
"""

x = 5
def my_fun():
    nonlocal x
    print(x)