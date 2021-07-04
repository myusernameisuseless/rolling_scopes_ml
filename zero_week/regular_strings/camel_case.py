"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
 The first word within the output should be capitalized only if the original word was capitalized
 (known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""
import re


def camel_case(string_):
    splitted = re.split('[-_]', string_)
    result = ''
    i = 0
    while i < len(splitted):
        if i == 0:
            result = result + splitted[i]
        else:
            result = result + splitted[i].capitalize()
        i += 1
    print(result)
    return result




camel_case('The-stealth-warrior_Warrior_lol_KEK')
