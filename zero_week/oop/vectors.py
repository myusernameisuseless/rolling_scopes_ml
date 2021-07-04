"""
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)'
(in Python, this is a __str__ method, so that str(a) == '(1,2,3)')

an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.
"""


class Vector(list):

    def __init__(self, vector):
        super().__init__()
        self.vector = vector

    def __str__(self):
        return f"{self.vector}"

    def __len__(self):
        return len(self.vector)

    def check_index(self, index):
        if index < -len(self.vector) or index >= len(self.vector):
            return False
        else:
            return True

    def __getitem__(self, value):
        if not self.vector:
            return 'IndexError'
        if self.check_index(value):
            return self.vector[value]
        else:
            return 'IndexError'

    def add(self, second):
        result = []
        print(len(second))
        try:
            for i in range(0, len(second)):
                result.append(self.vector[i] + second[i])
            print(result)
            return result
        except IndexError:
            print('IndexError')

    def subtract(self, second):
        result = []
        print(len(second))
        try:
            for i in range(0, len(second)):
                result.append(self.vector[i] - second[i])
            print(result)
            return result
        except IndexError:
            print('IndexError')

    def dot(self, second):
        result_list = []
        print(len(second))
        try:
            for i in range(0, len(second)):
                result_list.append(self.vector[i] * second[i])
            result = sum(result_list)
            print(result)
            return result
        except IndexError:
            print('IndexError')

    def norm(self):
        squared_result = 0
        for each in self.vector:
            squared_result += each ** 2
        result = squared_result ** 0.5
        print(result)
        return result


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)
