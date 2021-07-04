"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) === 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
                       // and 4 has only one digit
 persistence(999) === 4 // because 9*9*9 = 729, 7*2*9 = 126,
                        // 1*2*6 = 12, and finally 1*2 = 2
 persistence(4) === 0 // because 4 is already a one-digit number
"""
import numpy as np


count = 0


def persistence(number):
    digits_list = []
    if number < 0 or isinstance(number, str):
        print('Your input is incorrect!')
    elif number < 10:
        print("Persistance for your integer is: 0")
    else:
        for digit in str(number):
            digits_list.append(int(digit))
        result = ((np.prod(np.array(digits_list))).item())
        result_list = []
        for elem in str(result):
            result_list.append(int(elem))
        print(result_list)
        global count
        count += 1
        if len(result_list) != 1:
            persistence(result)
        else:
            print("Persistance for your integer is: ", count)


persistence(999)
