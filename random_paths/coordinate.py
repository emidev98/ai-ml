class Coordinate:

    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
    
    def move(self, delta_x : int, delta_y : int):
        return Coordinate(self.x + delta_x, self.y + delta_y)

    def distance(self, coordinate) -> int:
        delta_x = self.x - coordinate.x
        delta_y = self.y - coordinate.y
        
        return (delta_x**2 + delta_y**2)**0.5