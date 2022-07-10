"""
This is an example for a recursive function that
prints the next number n+1 up to the second 
multiple (2n).
"""

x = 10

def print_next_n(n):
    print(n+1)
    if n + 1 == x * 2 :
        #Terminal case
        return print("The second multiple of {} is {}".format(x,n+1))

    #Recursive case 
    return print_next_n(n+1)

print_next_n(x)