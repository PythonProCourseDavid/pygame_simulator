import pygame
import pygame.font

FONT_SIZE = 30
BLACK_COLOR = (0, 0, 0)
INFECTED_TEXT_COORDINATES = (10, 10)
INCUBATING_TEXT_COORDINATES = (160, 10)
HEALTH_TEXT_COORDINATES = (320, 10)


class UserInterface:
    def __init__(self, width, height, population, infection):
        self.width = width
        self.height = height
        self.population = population
        self.infection = infection
        self.font = pygame.font.SysFont(None, FONT_SIZE)

    def draw(self, screen):
        infected_count = self.population.get_infected_count()
        incubating_count = self.population.get_incubation_count()
        health_count = self.population.get_health_count()

        infected_counter = self.font.render(f"Infected: {infected_count}", True, BLACK_COLOR)
        incubating_counter = self.font.render(f"Incubating: {incubating_count}", True, BLACK_COLOR)
        health_counter = self.font.render(f"Health: {health_count}", True, BLACK_COLOR)

        screen.blit(infected_counter, INFECTED_TEXT_COORDINATES)
        screen.blit(incubating_counter, INCUBATING_TEXT_COORDINATES)
        screen.blit(health_counter, HEALTH_TEXT_COORDINATES)
