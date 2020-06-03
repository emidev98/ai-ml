class Rectangle:
    def __init__(self, width, height):
        self._width = width;
        self._height = height;

    def area(self):
        return self._width * self._height

class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, width)


if __name__ == '__main__':
    rectangle = Rectangle(3,5)
    square = Square(4)
    
    print(f"Rectangle area is {rectangle.area()}")
    print(f"Square area is {square.area()}")

    
    