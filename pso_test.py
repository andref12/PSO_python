import numpy as np
from funccusto import func_custo
import random
import time


def pso_run():
    range_xy = (0, 5)
    n_dim = 2
    n_particles = 10
    n_iterations = 30
    w = 0.9
    c1 = 0.5
    c2 = 1.5
    vmax = 0.25
    vmin = -vmax
    random.seed(time.time())
    pos_par = np.zeros((n_dim, n_particles))
    vel = np.zeros((n_dim, n_particles))
    x_plot = np.zeros((n_particles, n_iterations))
    y_plot = np.zeros((n_particles, n_iterations))
    for count_xy in range(0, n_particles):
        for count_dim in range(0, n_dim):
            pos_par[count_dim][count_xy] = random.randrange(range_xy[0]*100, range_xy[1]*100, 1)
    pos_par = np.divide(pos_par, 100)
    best_pos = np.zeros((1, n_dim))
    best_local_pos = pos_par
    best_z = -18
    best_z_local = np.zeros((1, n_particles))
    for count_init in range(0, n_particles):
        best_z_local[0][count_init] = func_custo(pos_par[0][count_init], pos_par[1][count_init])
        if best_z_local[0][count_init] > best_z:
            best_z = best_z_local[0][count_init]
            best_pos[0][0] = pos_par[0][count_init]
            best_pos[0][1] = pos_par[1][count_init]
    for it in range(0, n_iterations):
        for count_insert in range(0, n_particles):
            x_plot[count_insert][it] = pos_par[0][count_insert]
            y_plot[count_insert][it] = pos_par[1][count_insert]
        for par in range(0, n_particles):
            for dim in range(0, n_dim):
                r1 = random.randrange(0, 100, 1)
                r1 = r1/100
                r2 = random.randrange(0, 100, 1)
                r2 = r2 / 100
                vel[dim][par] = w * vel[dim][par] + c1*r1*(-pos_par[dim][par]+best_local_pos[dim][par]) + c2*r2*(-pos_par[dim][par] + best_pos[0][dim])
                if vel[dim][par] > vmax:
                    vel[dim][par] = vmax
                if vel[dim][par] < vmin:
                    vel[dim][par] = vmin
                pos_par[dim][par] = vel[dim][par] + pos_par[dim][par]
                if pos_par[0][par] > range_xy[1]:
                    pos_par[dim][par] = range_xy[1]
                if pos_par[1][par] < range_xy[0]:
                    pos_par[dim][par] = range_xy[0]
        for par2 in range(0, n_particles):
            y_ret = func_custo(pos_par[0][par2], pos_par[1][par2])
            if y_ret > best_z:
                best_z = y_ret
                best_pos[0][0] = pos_par[0][par2]
                best_pos[0][1] = pos_par[1][par2]
            if y_ret > best_z_local[0][par2]:
                best_z_local[0][par2] = y_ret
                best_local_pos[0][par2] = pos_par[0][par2]
                best_local_pos[1][par2] = pos_par[1][par2]
    return n_particles, x_plot, y_plot
