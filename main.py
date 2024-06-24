import pygame
from graphics.start_screen import StartScreen

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

start_screen = StartScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
running = True

while running:
    start_screen.run()

    if not start_screen.running:
        screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()