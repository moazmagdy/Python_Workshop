"""
This script includes implementations of filter function.
"""
#We use filter function to return only odd numbers
#from a list of numbers
nums = [1,2,3,4,5,6,7,8,9]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
sorted(odd_nums, reverse= True)

#We use filter function to sum all multiples of 3 in 
#numbers under 1000.
nums = list(range(1000))
sum_multiplies = sum(list(filter(lambda x: x % 3 == 0, nums)))