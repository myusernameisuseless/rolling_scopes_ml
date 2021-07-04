"""
You are asked to square every digit of a number and concatenate them.
"""


def squared_number(number):
    digits_list = []
    if number < 0 or isinstance(number, str):
        print('Your input is incorrect!')
    else:
        for digit in str(number):
            digit = pow(int(digit), 2)
            digits_list.append(digit)
    squared_string = ''.join([str(i) for i in digits_list])
    squared_num = int(squared_string)
    print(squared_num)


squared_number(456)
