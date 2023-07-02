from background import bgimage
from pso_test import pso_run
import pygame


light_blue = (68, 85, 90)
n_par, x_frame_pos, y_frame_pos = pso_run()
bgimage()
pygame.init()
Display = pygame.display.set_mode((369, 369))
pygame.display.set_caption('Particle Swarm')
BG = pygame.image.load("bg.png")
Display.blit(BG, (0, 0))
frame = 0
while 1:
    clock = pygame.time.Clock()
    if frame < 30:
        for par in range(0, n_par):
            x = 3.69*((x_frame_pos[par][frame]*100)/5)
            y = 3.69*((y_frame_pos[par][frame]*100)/5)
            x = round(x)
            y = round(y)
            pygame.draw.circle(Display, light_blue, (x, y), 5)
    if frame > 29:
        for par2 in range(0, n_par):
            x = 3.69 * ((x_frame_pos[par2][29] * 100) / 5)
            y = 3.69 * ((y_frame_pos[par2][29] * 100) / 5)
            x = round(x)
            y = round(y)
            pygame.draw.circle(Display, light_blue, (x, y), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    frame = frame + 1
    pygame.display.update()
    Display.blit(BG, (0, 0))
    clock.tick(5)
