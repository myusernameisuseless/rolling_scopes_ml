"""
You're going on a trip with some students and it's up to you to keep track of how much money each Student has.
A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student
with the most money. If every student has the same amount, then return "all".

Notes:

Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money
"""


class Student:
    money_list = []
    students_list = []

    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        self.money = (fives * 5) + (tens * 10) + (twenties * 20)
        self.money_list.append(self.money)
        self.students_list.append(self.name)

    def __str__(self):
        return f"{self.name}: {self.money}"

    @classmethod
    def richest(cls):
        if len(cls.money_list) > 1:
            if len(set(cls.money_list)) == 1:
                print('All!')
                return "All!"
            else:
                richest_money = max(cls.money_list)
                index = cls.money_list.index(richest_money)
                print(cls.students_list[index])
                return cls.students_list[index]
        else:
            print(cls.students_list[0])
            return cls.students_list[0]


st1 = Student('Ivan', 50, 50, 50)
st2 = Student('Cary', 50, 50, 50)
Student.richest()

