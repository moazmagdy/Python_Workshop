"""
This is an integer class which has an additional method that check if it's divisible by a certain number.
"""

class special_int(int):
    def is_divisible(self, x):
        return self % x == 0

my_int = special_int(8)
print(my_int.is_divisible(4))