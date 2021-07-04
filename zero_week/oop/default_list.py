"""
The collections module has defaultdict, which gives you a default value for trying to get the value of a key
which does not exist in the dictionary instead of raising an error. Why not do this for a list?

Your job is to create a class (or a function which returns an object) called DefaultList.
The class will have two parameters to be given: a list, and a default value.
The list will obviously be the list that corresponds to that object.
The default value will be returned any time an index of the list is called in the code
that would normally raise an error (i.e. i > len(list) - 1 or i < -len(list)).
This class must also support the regular list functions extend, append, insert, remove, and pop.

Because slicing a list never raises an error (slicing a list between two indexes
that are not a part of the list returns [], slicing will not be tested for.

Example
lst = DefaultList(['hello', 'abcd', '123', 123, True, False], 'default_value')
lst[4] = True
lst[80] = 'default_value'
lst.extend([104, 1044, 4066, -2])
lst[9] = -2
"""


class DefaultList(list):

    def __init__(self, list_, default_value=None):
        super().__init__()
        self.list_ = list_
        self.default_value = default_value

    def check_index(self, index):
        if index < -len(self.list_) or index >= len(self.list_):
            return False
        else:
            return True

    def __getitem__(self, value):
        if not self.list_:
            return self.default_value
        if self.check_index(value):
            return self.list_[value]
        else:
            return self.default_value


test_list = DefaultList([1, 2, 3, 4, 5], 'default value')
print(test_list[10])
