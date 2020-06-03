from .person import Person, BasicPerson
from .coordinate import Coordinate
from .path import Path
from .charting import Charting

class Init():

    def __init__(self, total_number_of_steps = [1000000], number_of_tries = 1, type_of_person = BasicPerson):
        self.total_number_of_steps = total_number_of_steps
        self.number_of_tries = number_of_tries
        self.type_of_person = type_of_person
        self.charting = Charting(total_number_of_steps)
        
        for steps in total_number_of_steps:
            distances = self.simulate_walking(steps, type_of_person)
            average_distance = round(sum(distances) / len(total_number_of_steps), 4)
            max_distance = max(distances)
            min_distance = min(distances)

            self.charting.append_average_distance(average_distance)
            print(f"{type_of_person.__name__} walked {steps} steps\t| (distance) Average: {average_distance}\tMax: {max_distance}\tMin: {min_distance}")

        if len(total_number_of_steps) > 1:
            self.charting.show_average_chart()
        else:
            self.charting.show_path_chart()

        
    def simulate_walking(self, steps: int, type_of_person: Person):
        person = type_of_person(name="Emi")
        origin = Coordinate(0,0)
        distances = []
        
        for _ in range(self.number_of_tries):
            path = Path()
            path.add_person(person,origin)
            simulate_walking = self.walk(path, person, steps)
            distances.append(round(simulate_walking,1))
        
        return distances


    def walk(self, path : Path, person : Person, steps : int) -> int:
        start = path.get_coordinate(person)

        for _ in range(steps):
            path.move_person(person)
            new_coordinate = path.get_coordinate(person)
            self.charting.append_steps_coordinates_in_path(new_coordinate)
            
        distance = path.get_coordinate(person)
        return start.distance(distance)

if __name__ == '__main__':
    number_of_tries = int(input("How many times do you want to execute each path? "))
    total_number_of_steps = []
    do_more_steps = True

    while do_more_steps:
        steps_per_path_question = input("What is the number of steps that you want to walk per path (type 'start' to start the execution)? ")

        if steps_per_path_question.isnumeric():
            total_number_of_steps.append(int(steps_per_path_question))
        elif steps_per_path_question == "start":
            do_more_steps = False

    Init(total_number_of_steps,number_of_tries)
    Init()