"""
Your job is to create a class Dictionary which you can add words to and their entries. Example:

d = Dictionary()

d.new_entry('Apple', 'A fruit that grows on trees')

print(d.look('Apple'))
A fruit that grows on trees

print(d.look('Banana'))
Can't find entry for Banana
"""


class Dictionary:

    def __init__(self):
        self.dict_ = {}

    def new_entry(self, key, value):
        new = self.dict_.update([(key, value)])
        return new

    def look(self, key):
        look = self.dict_.get(key, "Can't find entry for Banana")
        return look


d = Dictionary()

d.new_entry('Apple', 'A fruit that grows on trees')

print(d.look('Apple'))

print(d.look('Banana'))
