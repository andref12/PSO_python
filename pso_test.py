import numpy as np
from costfunc import cost_func
import random
import time

class pso_run():
    def __init__(self, start = 0, finish = 5, particles = 10, iterations = 30, inertia = 0.9, cognitive_c = 0.5, social_c = 1.5, max_vel = 0.25):
        self.range_xy = (start, finish)
        self.n_dim = 2
        self.n_particles = particles
        self.n_iterations = iterations
        self.w_inertia = inertia
        self.cognitive_coefficient = cognitive_c
        self.social_coefficient = social_c
        self.v_max = max_vel
        self.v_min = -self.v_max
        self.best_z = 0
        
        self.best_z_local = np.zeros((1, self.n_particles))
        self.pos_par = np.zeros((self.n_dim, self.n_particles))
        self.best_local_pos = np.zeros((self.n_dim, self.n_particles))
        self.best_pos = np.zeros((1, self.n_dim))
        self.vel = np.zeros((self.n_dim, self.n_particles))
        self.x_plot = np.zeros((self.n_iterations, self.n_particles))
        self.y_plot = np.zeros((self.n_iterations, self.n_particles))
        random.seed(time.time())

    def init_particles_random_pos(self):
        for count_xy in range(0, self.n_particles):
            for count_dim in range(0, self.n_dim):
                self.pos_par[count_dim][count_xy] = random.randrange(self.range_xy[0]*100, self.range_xy[1]*100, 1)
        self.pos_par = np.divide(self.pos_par, 100)
        self.best_local_pos = self.pos_par

        for count_init in range(0, self.n_particles):
            self.best_z_local[0][count_init] = cost_func(self.pos_par[0][count_init], self.pos_par[1][count_init])
        self.best_z = np.max(self.best_z_local)
        self.best_pos = self.best_local_pos[:,np.argmax(self.best_z_local)]

    def update_particles_positions(self):
        for par in range(0, self.n_particles):
            for dim in range(0, self.n_dim):
                r1 = (random.randrange(0, 100, 1)) / 100
                r2 = (random.randrange(0, 100, 1)) / 100
                self.vel[dim][par] = self.w_inertia * self.vel[dim][par] + self.cognitive_coefficient*r1*(-self.pos_par[dim][par]+self.best_local_pos[dim][par]) + self.social_coefficient*r2*(-self.pos_par[dim][par] + self.best_pos[dim])
                self.check_velocity_in_range(dim,par)
                self.pos_par[dim][par] = self.vel[dim][par] + self.pos_par[dim][par]
                self.check_position_in_range(dim,par)
    
    def check_velocity_in_range(self,dim,par):
        if self.vel[dim][par] > self.v_max:
            self.vel[dim][par] = self.v_max
        if self.vel[dim][par] < self.v_min:
            self.vel[dim][par] = self.v_min

    def check_position_in_range(self,dim,par):
        if self.pos_par[0][par] > self.range_xy[1]:
            self.pos_par[dim][par] = self.range_xy[1]
        if self.pos_par[1][par] < self.range_xy[0]:
            self.pos_par[dim][par] = self.range_xy[0]

    def pso_iterations(self):
        for it in range(0, self.n_iterations):      
            self.x_plot[it][:] = self.pos_par[0][:]
            self.y_plot[it][:] = self.pos_par[1][:]
            self.update_particles_positions()
            self.check_personal_global_best()
        return self.x_plot.T, self.y_plot.T

    def check_personal_global_best(self):
        for par in range(0, self.n_particles):
            y_ret = cost_func(self.pos_par[0][par], self.pos_par[1][par])
            if y_ret > self.best_z:
                self.best_z = y_ret
                self.best_pos[0] = self.pos_par[0][par]
                self.best_pos[1] = self.pos_par[1][par]
            if y_ret > self.best_z_local[0][par]:
                self.best_z_local[0][par] = y_ret
                self.best_local_pos[0][par] = self.pos_par[0][par]
                self.best_local_pos[1][par] = self.pos_par[1][par]
