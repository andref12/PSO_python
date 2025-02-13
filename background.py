import numpy as np
import matplotlib.pyplot as plt
from costfunc import cost_func


def create_bg_image(start, finish, step = 0.01):
    x = np.arange(start, finish, step)
    y = np.arange(start, finish, step)
    len_x = len(x)
    z = np.zeros([len_x, len_x])
    for count_x in range(1, len_x):
        for count_y in range(1, len_x):
            z[count_x][count_y] = cost_func(y[count_y], x[count_x])

    plt.axis('off')
    plt.imshow(z, cmap='Spectral')
    plt.savefig('bg.png', bbox_inches='tight', pad_inches=0)