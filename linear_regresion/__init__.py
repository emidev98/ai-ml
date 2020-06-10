import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x, y):
    n = np.size(x)

    # calculate the average of x and y
    m_x, m_y = np.mean(x), np.mean(y)

    # Calculate the sum of xy and xx
    sum_xy = np.sum((x - m_x) * (y - m_y))
    sum_xx = np.sum(x * (x - m_x))

    # calculate the coefficient of the regresion
    b_1 = sum_xy / sum_xx
    b_0 = m_y - (b_1 * m_x)

    return (b_0, b_1)

def plot_regression(x, y, b):
    plt.scatter(x, y, color = "g", marker = "o", s = 30)

    y_pred = b[0] + (b[1] * x)

    plt.plot(x, y_pred, color = "b")

    plt.xlabel("X - Independent")
    plt.xlabel("Y - Dependent")

    plt.show()


if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 6, 5])

    b = estimate_b0_b1(x, y)
    print(b)

    plot_regression(x, y, b)

    # coefficient = np.polyfit(x, y, 1)

    # m = coefficient[0]
    # b = coefficient[1]
    # est_y = (m * x) + b

    # plt.plot(x, est_y)
    # plt.scatter(x, y)
    # plt.show()