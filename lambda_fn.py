"""
This script include different implementations for Lambda functions.
"""
#Lambda function to sum two input variables
from nis import cat


add_up = lambda x,y: print(x+y)
add_up(5,3)

#Lambda function to return the first item in list.
first_item = lambda x: x[0]
first_item(['dog', 'mouse', 'cat'])

