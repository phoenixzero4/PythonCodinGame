import math
import sys

''' 
Given an array of integers, can each index in the array be traversed exactly once by jumping ahead the number of indices represented by the integer in the array index you land on.

For example, beginning at index 0 in array [1, 2, 2, 1, 3], you would then jump 1 slot to array[1] which is 2. Then you would jump to array[3] which contains 1. Jumping 1 space to array[5] which is 3 brings you around in the array to array[2] which is the last array index to be visited.
'''
def main():
    l = input("Enter space separated integers for the array:\n")
    array = list()
    for i in l.split():
        array.append(int(i))
        n = len(array)
    j = 0
    cycle = True
    for i in range(n):
        if j >= n:
            j = j % n
        if array[j] is None:
            cycle = False
        else:
            temp = j
            j = j + array[j]
            array[temp] = None
    print(cycle)

main()

        
