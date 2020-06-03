class Person:
    def __init__(self, name):
        self._name = name

    def go_forward(self):
        print("Walking")

class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)
    
    def go_forward(self):
        print("Pedaling")


def main():
    person = Person("David")
    cyclist = Cyclist("Emi")
    person.go_forward()
    cyclist.go_forward()

if __name__ == '__main__':
    main();