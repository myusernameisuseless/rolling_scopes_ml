"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

len(array[0])
"""
import numpy as np

snail_list = []


def snail(array):
    global snail_list
    n = len(array)
    m = len(array[0])
    i = 0
    j = 0
    while j <= m - 1:
        snail_list.append(array[0][j])
        j += 1
    array.remove(array[0])
    rotated = (np.rot90(array)).tolist()
    if len(rotated) > 1:
        snail(rotated)
    elif len(rotated) == 1:
        snail_list.append(rotated[0][0])
        print(snail_list)
        return snail_list


snail([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
