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
    found = False   #Binary value to control iterations
    slice_start = 0       #Start index of sublist
    slice_end = len(x) - 1    #End index of sublist
    while slice_start <= slice_end and not found:
        location = (slice_start + slice_end) // 2
        if x[location] == search_value:
            found = True
        else:
            if search_value < x[location]:
                slice_end = location - 1
            else:
                slice_start = location + 1

    if __name__ == '__main__':
        print("Your search value of {0} is in index {1}".format(search_value, location))
    else:
        print("{0} is not in {1}".format(search_value, x))

  