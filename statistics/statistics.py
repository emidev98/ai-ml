import random
import math

def average(x):
    return sum(x) / len(x)

def variance(X):
    mu = average(X)
    
    accumulator = 0
    for x in X:
        accumulator += (x - mu)**2
    
    return accumulator / len(X)

def standard_deviation(X):
    return math.sqrt(variance(X))

if __name__ == '__main__':
    X = [random.randint(1,100) for i in range(100)]
    mu = average(X)
    Var = variance(X)
    standard_deviation = standard_deviation(X)

    print(f"{X}\naverage = {mu} | variance = {Var} | standard deviation = {standard_deviation}")