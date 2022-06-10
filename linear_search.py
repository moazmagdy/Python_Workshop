"""
This file implements the linear search algorithm which
works as follows:
1. Start with a list of numbers.
2. Specify a value to search_for.
3. Create a result variable that has a default value of -1. If the search is unsuccessful,
this value will remain -1 after the algorithm is executed.
4. Loop through the list. If the value equals the search value, set the result, and exit
the loop.
"""

from unittest import result


def linear_search(x, search_value):
    for i in range(len(x)):
        if x[i] == search_value:
            result = i
            break
    if __name__ == '__main__':
        print("Search value of {0} is in index {1}".format(search_value, result))