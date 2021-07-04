"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""


def odd_integer(list_):
    odd_number = 0
    if not isinstance(list_, list):
        print("Your input is incorrect!")
    else:
        for elem in list_:
            count = list_.count(elem)
            if count % 2 == 0:
                continue
            else:
                odd_number = elem
    print('Integer that appears an odd number of times in this list is: ', odd_number)


odd_integer([1, 2, 3, 5, 5, 1, 2, 3, 4, 4, 5, 5, 5])
