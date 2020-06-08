import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__init__':
    x = np.array(list(range(0,9)))
    y = np.array([1,2,3,5,4,6,8,7,9])

    coefficient = np.polyfit(x, y, 1)

    m = coefficient[0]
    b = coefficient[1]
    est_y = (m * x) + b

    plt.plot(x, est_y)
    plt.scatter(x, y)
    plt.show()