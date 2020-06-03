from .person import Person
from .coordinate import Coordinate

class Path:

    def __init__(self):
        self.coordinates = {}

    def add_person(self, person : Person, coordinate : Coordinate):
        self.coordinates[person] = coordinate

    def move_person(self, person : Person):
        delta_x, delta_y = person.walk_randomly()
        current_coordinate = self.coordinates[person]
        new_coordinate = current_coordinate.move(delta_x, delta_y)

        self.coordinates[person] = new_coordinate
    
    def  get_coordinate(self, person : Person) -> Coordinate:
        return self.coordinates[person]