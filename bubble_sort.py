"""
This file implements the bubble sort algorithm which works as follows:
1. Start with the first two elements of this list. If the first is larger than the second, then switch the positions of the numbers.
2. Then, move onto the next two elements and compare them and switch positions.
3. Continue utill you reach the end.
4. Then, repeat steps 1 to 3 until no more swaps.
"""
def bubbleSort(x):
    y =[0]*len(x)
    while True:
        for i in x:
            if  x[i] > x[i+1]:
                y[i], y[i+1] = x[i+1], x[i]
            else:
                y[i], y[i+1] = x[i], x[i+1]
            

    if __name__ == '__main__':
        print(x)