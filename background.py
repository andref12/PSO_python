import numpy as np
import matplotlib.pyplot as plt
from funccusto import func_custo


def bgimage():
    step = 0.01
    x = np.arange(0, 5, step)
    y = np.arange(0, 5, step)
    lenx = len(x)
    z = np.zeros([lenx, lenx])
    for countx in range(1, lenx):
        for county in range(1, lenx):
            z[countx][county] = -func_custo(x[countx], y[county])
    plt.axis('off')
    plt.imshow(z, cmap='Spectral')
    plt.savefig('bg.png', bbox_inches='tight', pad_inches=0)