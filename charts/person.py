from random import choice

class Person:

    def __init__(self, name : str):
        self.name = name;


class BasicPerson(Person):

    def __init__(self, name : str):
        super().__init__(name)

    def walk(self):
        paths = [(0, 1), (0, -1), (1, 0), (-1, 0)] # TOP / BOTTOM / RIGHT / LEFT
        return choice(paths)