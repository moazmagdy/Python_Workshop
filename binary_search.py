"""
This script implements the binary search algorithm
which works as follows:
1. Input is a sorted array.
2. Take the midpoint of the list. If this value is less than the target value, discard the
left half of the list, and vice versa.
3. You repeat this process with the remaining side of the list, picking the midpoint of the
remaining values.
"""

def binary_search(x, search_value):
    still_divisble = True
    mid_pt = len(x)//2
    if search_value in x:
        while still_divisble:
            still_divisble = False
            if x[mid_pt] < search_value:
                mid_pt += int((len(x)-mid_pt))
                still_divisble = True
            elif x[mid_pt] > search_value:
                mid_pt -= int((len(x)-mid_pt))
                still_divisble = True
            else:
                result = mid_pt
        if __name__ == '__main__':

            print("Your search value of {0} is in index {1}".format(search_value, result))
    else:
        print("{0} is not in {1}".format(search_value, x))

  