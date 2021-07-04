"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""


def delete_vowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    without_vowels = []
    without_vowels_str = ''
    for letter in string_:
        if letter not in vowels:
            without_vowels.append(letter)
    without_vowels_str = without_vowels_str.join(without_vowels)
    print(without_vowels_str)
    return without_vowels_str


delete_vowel('asdasdasdA asaaa! LOL')
