from pso_test import pso_run
from background import create_bg_image
import pygame

light_blue = (68, 85, 90)

class pygame_run():
    def __init__(self, start = 0, finish = 5, particles = 10, iterations = 30, inertia = 0.9, cognitive_c = 0.5, social_c = 1.5, max_vel = 0.25):
        self.n_pso_iterations = iterations
        self.n_par = particles
        self.lower_bound = start
        self.upper_bound = finish

        pso = pso_run(start, finish, particles, iterations, inertia, cognitive_c, social_c, max_vel)
        pso.init_particles_random_pos()
        self.x_frame_pos, self.y_frame_pos = pso.pso_iterations()

        create_bg_image(self.lower_bound, self.upper_bound)

        self.display_size = (369,369)
        pygame.init()
        self.pygame_display = pygame.display.set_mode(self.display_size)
        pygame.display.set_caption('Particle Swarm')
        self.cost_func_heat_map = pygame.image.load("bg.png")
        self.pygame_display.blit(self.cost_func_heat_map, (0, 0))

    def pygame_animation(self):
        frame = 0
        while 1:
            clock = pygame.time.Clock()
            if frame < (self.n_pso_iterations - 1):
                for par in range(0, self.n_par):
                    x = self.adjust_to_display_pygame(self.x_frame_pos[par][frame])
                    y = self.adjust_to_display_pygame(self.y_frame_pos[par][frame])
                    pygame.draw.circle(self.pygame_display, light_blue, (x, y), 5)
            elif frame >= (self.n_pso_iterations - 1):
                for par2 in range(0, self.n_par):
                    x = self.adjust_to_display_pygame(self.x_frame_pos[par2][self.n_pso_iterations - 1])
                    y = self.adjust_to_display_pygame(self.y_frame_pos[par2][self.n_pso_iterations - 1])
                    pygame.draw.circle(self.pygame_display, light_blue, (x, y), 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            frame += 1
            pygame.display.update()
            self.pygame_display.blit(self.cost_func_heat_map, (0, 0))
            clock.tick(5)

    def adjust_to_display_pygame(self,input):
        graph_size = (self.upper_bound - self.lower_bound)
        ajusted_value = (self.display_size[1])*((input)/graph_size)
        return round(ajusted_value)

test = pygame_run(particles = 10)
test.pygame_animation()