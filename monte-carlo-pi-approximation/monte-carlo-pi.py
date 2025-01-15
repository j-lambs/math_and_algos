import numpy as np
import matplotlib.pyplot as plt

n1 = 10
n2 = 30
n3 = 100
n4 = 1000
n5 = 100000
n6 = 1000000

# area of interest: within square with vertecies at...
# (1, 1), (1, - 1), (-1, -1), (-1, 1)
# return: list of tuples representing cartesian coordinates
def get_random_values_in_area(lo, hi, n):
    rng = np.random.default_rng(seed=2025)
    unif_x = rng.uniform(lo, hi, n)  # x-values
    unif_y = rng.uniform(lo, hi, n)  # y-values
    return list(zip(unif_x, unif_y)) # merges 2 lists into single list of tuples

# determines whether data point, d, is in unit circle or not
# return: true when inside unit circle
def in_unit_circle(c):
    if abs(c[1]) <= (1 - c[0]**2)**0.5:
        return 1
    else:
        return 0
        
# return: approximated pi
def approximate_pi(samples: list, n):
    tf = []
    for dp in samples:
        tf.append(in_unit_circle(dp))
    return 4 * sum(tf) / n 

data = get_random_values_in_area(-1, 1, n5)
print(approximate_pi(data, n5))

# Reference: pi = 3.1415926536...
