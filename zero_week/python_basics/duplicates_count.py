"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
that occur more than once in the input string. The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicates_count(string_):
    string_ = string_.casefold()
    list_of_symbols = []
    count_list = []
    symbols_count = {}
    for elem in string_:
        list_of_symbols.append(elem)
        count = list_of_symbols.count(elem)
        count_list.append(count)
        symbols_count.update({elem: count})
    print(symbols_count.items())
    duplicates = []
    for value in symbols_count.values():
        if value > 1:
            duplicates.append(value)
    print('The number of duplicates is: ', len(duplicates))
    number_of_duplicates = len(duplicates)
    return number_of_duplicates


duplicates_count('abcdeEE')
