import pygame


HOUSE_COLOR = (100, 100, 100)
WHITE_COLOR = (255, 255, 255)
WINDOW_COLOR = (0, 0, 255, 255)
DOOR_COLOR = (190, 190, 190, 255)
BLACK_COLOR = (0, 0, 0, 255)


class City:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.houses = [
            pygame.Rect(50, 50, 100, 100),
            pygame.Rect(5, 190, 60, 110),
            pygame.Rect(200, 100, 100, 50),
            pygame.Rect(260, 50, 40, 65),
            pygame.Rect(200, 200, 75, 110),
            pygame.Rect(410, 100, 120, 100),
            pygame.Rect(600, 300, 110, 100),
            pygame.Rect(400, 280, 40, 40),
            pygame.Rect(400, 240, 40, 40),
            pygame.Rect(400, 320, 40, 40),
            pygame.Rect(440, 280, 40, 40),
            pygame.Rect(360, 280, 40, 40),
            pygame.Rect(100, 400, 125, 65),
            pygame.Rect(5, 500, 50, 50),
            pygame.Rect(500, 500, 130, 60),
            pygame.Rect(300, 400, 90, 100),
            pygame.Rect(700, 150, 100, 110),
            pygame.Rect(540, 110, 110, 110)
        ]

        self.windows = [
            pygame.Rect(60, 65, 20, 20),
            pygame.Rect(90, 65, 20, 20),
            pygame.Rect(120, 65, 20, 20),
            pygame.Rect(60, 90, 20, 20),
            pygame.Rect(90, 90, 20, 20),
            pygame.Rect(120, 90, 20, 20),
            pygame.Rect(60, 115, 20, 20),
            pygame.Rect(120, 115, 20, 20),
        ]

        self.doors = [
            pygame.Rect(92.7, 115, 15, 35)
        ]

        self.knobs = [
            pygame.Rect(100, 130, 3, 3)
        ]

        self.square = [
            pygame.Rect(405, 285, 5, 30),
            pygame.Rect(430, 285, 5, 30),
            pygame.Rect(410, 297, 20, 5)
        ]

    def draw(self, screen):
        for house in self.houses:
            pygame.draw.rect(screen, HOUSE_COLOR, house)

        for square in self.square:
            pygame.draw.rect(screen, WHITE_COLOR, square)

        for window in self.windows:
            pygame.draw.rect(screen, WINDOW_COLOR, window)

        for door in self.doors:
            pygame.draw.rect(screen, DOOR_COLOR, door)

        for knob in self.knobs:
            pygame.draw.rect(screen, BLACK_COLOR, knob)
