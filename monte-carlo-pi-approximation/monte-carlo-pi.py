import math
import numpy as np
import matplotlib.pyplot as plt

MAX_N = 10000
step = 10
list_n = list(range(step, MAX_N + 1, step))

# area of interest: within square with vertices at...
# (1, 1), (1, - 1), (-1, -1), (-1, 1)
# return: list of tuples representing cartesian coordinates
def get_random_values_in_area(lo, hi, n):
    rng = np.random.default_rng()
    unif_x = rng.uniform(lo, hi, n)  # x-values
    unif_y = rng.uniform(lo, hi, n)  # y-values
    return (unif_x, unif_y)

# determines whether data point, d, is in unit circle or not
# return: true when inside unit circle
def in_unit_circle(x, y):
    if abs(y) <= (1 - x**2)**0.5:
        return 1
    else:
        return 0
        
# return: approximated pi
def approximate_pi(x_samples, y_samples, n):
    tf = []
    if (len(x_samples) == len(y_samples)):
        for i in range(len(x_samples)):
            tf.append(in_unit_circle(x_samples[i], y_samples[i]))

        sample_ratio = sum(tf) / n
        return 4 * sample_ratio


# ****************************************** MAIN ******************************************
if __name__ == "__main__": 

    # Show error (difference between approximate pi and 'true' pi) 
    errors = []
    for n in list_n:
        data = get_random_values_in_area(-1, 1, n)
        sample_pi = approximate_pi(data[0], data[1], n)
        errors.append(abs(math.pi - sample_pi))


    plt.plot(list_n, errors)
    plt.title("Distance from π as N increases")
    plt.xlabel("N")
    plt.ylabel("Distance from π")
    plt.show()

# Reference: pi = 3.1415926536...
