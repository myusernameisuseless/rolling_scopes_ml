"""
Your task is to make a function that can take any non-negative integer as an argument and
return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.
"""


def descending(number):
    digits_list = []
    if number < 0 or isinstance(number, str):
        print("Your input is incorrect!")
    else:
        for digit in str(number):
            digits_list.append(digit)
    sorted_digits_list = sorted(digits_list, reverse=True)
    sorted_string = ''.join([str(i) for i in sorted_digits_list])
    sorted_number = int(sorted_string)
    print(sorted_number)


descending(4724546)
