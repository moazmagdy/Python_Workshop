"""
This script includes implementations of Map function.
"""
#Here's a list of names and we need to return the
#number of characters in each name.
names = ['Ayman', 'Amr', 'Mahmoud', 'Awww']

#We use map function to apply len function to the
#whole list
lengths = list(map(len, names))

#Map a lambda function to a list of numbers to
#apply a logistic transformer

import math
numbers = [-3, -5, 1, 4]
nums_trans = list(map(lambda x: 1/(1+math.exp(-x)), numbers))
print(nums_trans)