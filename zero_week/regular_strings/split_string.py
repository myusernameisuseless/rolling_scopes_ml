"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character
of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


def split_string(string_):
    if len(string_) % 2 == 0:
        pass
    else:
        string_ += '_'
    result_list = []
    i = 0
    while i != len(string_):
        result_list.append(string_[i:i+2])
        i += 2
    print(result_list)


split_string('abcd')
