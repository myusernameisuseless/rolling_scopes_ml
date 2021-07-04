"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array,
containing the names of people who like an item.
It must return the display text as shown in the examples:

likes [] -- must be "no one likes this"
likes ["Peter"] -- must be "Peter likes this"
likes ["Jacob", "Alex"] -- must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] -- must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] -- must be "Alex, Jacob and 2 others like this"
"""


def likes(list_):
    if len(list_) == 0:
        print('No one likes this.')
    elif len(list_) == 1:
        print(f'{list_[0]} likes this.')
    elif len(list_) == 2:
        print(f'{list_[0]} and {list_[1]} like this.')
    elif len(list_) == 3:
        print(f'{list_[0]}, {list_[1]} and {list_[2]} like this.')
    else:
        print(f'{list_[0]}, {list_[1]} and {len(list_)-2} like this.')


likes(['Alex', 'Britney', 'William', 'Robert', 'Robin'])
