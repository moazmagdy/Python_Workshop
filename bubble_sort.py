"""
This file implements the bubble sort algorithm which works as follows:
1. Start with the first two elements of this list. If the first is larger than the second, then switch the positions of the numbers.
2. Then, move onto the next two elements and compare them and switch positions.
3. Continue utill you reach the end.
4. Then, repeat steps 1 to 3 until no more swaps.
"""
def bubbleSort(x):
    still_swapping = True
    while still_swapping:
        still_swapping = False
        for i in range(len(x)-1):
            if  x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                still_swapping = True

    if __name__ == '__main__':
        print(x)