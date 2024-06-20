import pygame
import random


WIDTH = 700
HEIGHT = 500
WHITE = (255, 255, 255)
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.wait(300000000)
    running = False

pygame.quit()