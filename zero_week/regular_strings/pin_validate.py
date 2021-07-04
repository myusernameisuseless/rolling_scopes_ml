"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false
"""


def pin_validate(pin):
    if not isinstance(pin, int):
        result = 'false'
        print(result)
        return result
    elif len(str(pin)) > 6 or len(str(pin)) < 4:
        result = 'false'
        print(result)
        return result
    else:
        result = 'true'
        print(result)
        return result


pin_validate(123452)
