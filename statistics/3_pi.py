import random
import math
from statistics import standard_deviation, average

def throw_needles(number_of_needles):
    needles_inside_circle = 0

    for _ in range(number_of_needles):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])

        distance_from_center = math.sqrt(x**2 + y**2) # Pythagorean theorem: https://en.wikipedia.org/wiki/Pythagorean_theorem

        if distance_from_center <= 1:
            needles_inside_circle += 1

    return (4 * needles_inside_circle) / number_of_needles

def simulate(number_of_needles, number_of_tries):
    pi_averages = []
    for _ in range(number_of_tries):
        pi_average = throw_needles(number_of_needles)
        pi_averages.append(pi_average)

    pi_average = average(pi_averages)
    strd_deviation = standard_deviation(pi_averages)

    print(f"Average={pi_average} | Standard Deviation={strd_deviation} | Number of needles={number_of_needles}")

    return (pi_average, strd_deviation)

def estimate_pi(precision, number_of_needles, number_of_tries):
    sigma = precision

    while sigma >= precision / 1.96:
        average, sigma = simulate(number_of_needles, number_of_tries)
        number_of_needles *= 2

    return average

if __name__ == '__main__':
    estimate_pi(0.01, 1000, 1000)