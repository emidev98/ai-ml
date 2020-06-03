from bokeh.plotting import figure, output_file, show
import random

if __name__ == '__main__':
    output_file('simple_chart.html')
    fig = figure()

    total_values = int(input("How many values do you want to generate in the chart? "))

    x = list(range(total_values))
    y = list(random.sample(range(0, total_values), total_values))
    
    fig.line(x, y, line_width=2)
    show(fig)