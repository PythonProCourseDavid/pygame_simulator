import pygame
from graphics.start_screen import StartScreen
from simulation.city import City
from simulation import Person, Population, Infection

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
        city = City(SCREEN_WIDTH, SCREEN_HEIGHT)
        population = Population(SCREEN_WIDTH, SCREEN_HEIGHT, city)
        infection = Infection(population)

        while running:
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            population.update()
            infection.update()

            city.draw(screen)
            population.draw(screen)

            if population.get_infected_count() == len(population.people):
                blurred_interface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                blurred_interface.set_alpha(150)
                blurred_interface.fill(WHITE)

                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

            pygame.display.flip()
            clock.tick(30)

pygame.quit()