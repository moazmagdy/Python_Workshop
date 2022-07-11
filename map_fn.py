"""
This script includes implementations of Map function.
"""
#Here's a list of names and we need to return the
#number of characters in each name.
names = ['Ayman', 'Amr', 'Mahmoud', 'Awww']

#We use map function to apply len function to the
#whole list
lengths = list(map(len, names))