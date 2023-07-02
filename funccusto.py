import numpy as np
import math


def func_custo(x, y):
    sin_1 = np.sin(3*x + 1.41)
    sin_2 = np.sin(4*y - 1.73)
    z = (x - 3.14)**2 + (y - 2.72)**2 + sin_1 + sin_2
    z = -z
    return z
