from .coordinate import Coordinate
from bokeh.plotting import figure, show

class Charting:

    def __init__(self,total_number_of_steps : list):
        self.total_number_of_steps = total_number_of_steps
        self.average_distances_per_run = []
        self.steps_coordinates_in_path = []

    def append_average_distance(self, coordinate : Coordinate):
        self.average_distances_per_run.append(coordinate)

    def append_steps_coordinates_in_path(self, steps_coordinates_in_path : Coordinate):
        self.steps_coordinates_in_path.append(steps_coordinates_in_path)
    
    def set_total_number_of_steps(self, total_number_of_steps):
        self.total_number_of_steps = total_number_of_steps

    def show_average_chart(self):
        chart = figure(title="Average chart", x_axis_label="steps", y_axis_label="distance")
        chart.line(self.total_number_of_steps, self.average_distances_per_run, legend_label="Average distance")
        show(chart)

    def show_path_chart(self):
        chart = figure(title="Path chart", x_axis_label="X axis", y_axis_label="Y axis")

        x_steps = []
        y_steps = []

        for coordinate in self.steps_coordinates_in_path:
            x_steps.append(coordinate.x)
            y_steps.append(coordinate.y)
        
        chart.line(x_steps, y_steps, legend_label="Path")
        show(chart)