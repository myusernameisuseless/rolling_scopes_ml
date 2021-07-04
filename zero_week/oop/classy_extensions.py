"""
Classy Extensions
Classy Extensions, this kata is mainly aimed at the new JS ES6 Update introducing extends keyword.
You will be preloaded with the Animal class, so you should only edit the Cat class.


Your task is to complete the Cat class which
Extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'

The name attribute is passed with self.name.
"""


class Cat:

    def __init__(self, _name):
        self.name = _name

    def speak(self):
        print(f'{self.name} meows.')
        meow = f'{self.name} meows.'
        return meow


cat1 = Cat('Mr Whiskers')
cat2 = Cat('Lamp')
cat3 = Cat('$$Money Bags$$')
cat1.speak()
cat2.speak()
cat3.speak()
