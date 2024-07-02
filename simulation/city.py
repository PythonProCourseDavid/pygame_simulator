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
            pygame.Rect(270, 65, 20, 25),
            pygame.Rect(270, 115, 20, 25),
            pygame.Rect(210, 115, 20, 25),
            pygame.Rect(210, 215, 20, 20),
            pygame.Rect(245, 215, 20, 20),
            pygame.Rect(210, 240, 20, 20),
            pygame.Rect(245, 240, 20, 20),
            pygame.Rect(210, 265, 20, 20),
            pygame.Rect(10, 200, 20, 25),
            pygame.Rect(40, 200, 20, 25),
            pygame.Rect(10, 233, 20, 25),
            pygame.Rect(40, 233, 20, 25),
            pygame.Rect(10, 266, 20, 25),
            pygame.Rect(7, 515, 20, 25),
            pygame.Rect(150, 405, 30, 20),
            pygame.Rect(110, 405, 30, 20),
            pygame.Rect(190, 405, 30, 20),
            pygame.Rect(110, 435, 30, 20),
            pygame.Rect(150, 435, 30, 20),
            pygame.Rect(305, 410, 20, 20),
            pygame.Rect(335, 410, 20, 20),
            pygame.Rect(365, 410, 20, 20),
            pygame.Rect(305, 440, 20, 20),
            pygame.Rect(335, 440, 20, 20),
            pygame.Rect(365, 440, 20, 20),
            pygame.Rect(335, 470, 20, 20),
            pygame.Rect(365, 470, 20, 20),
            pygame.Rect(415, 110, 20, 20),
            pygame.Rect(445, 110, 20, 20),
            pygame.Rect(475, 110, 20, 20),
            pygame.Rect(505, 110, 20, 20),
            pygame.Rect(415, 140, 20, 20),
            pygame.Rect(445, 140, 20, 20),
            pygame.Rect(475, 140, 20, 20),
            pygame.Rect(505, 140, 20, 20),
            pygame.Rect(415, 170, 20, 20),
            pygame.Rect(475, 170, 20, 20),
            pygame.Rect(505, 170, 20, 20),
            pygame.Rect(545, 115, 20, 20),
            pygame.Rect(575, 115, 20, 20),
            pygame.Rect(605, 115, 35, 20),
            pygame.Rect(545, 148, 35, 20),
            pygame.Rect(590, 148, 20, 20),
            pygame.Rect(620, 148, 20, 20),
            pygame.Rect(575, 181, 20, 20),
            pygame.Rect(605, 181, 35, 20),
            pygame.Rect(705, 155, 20, 20),
            pygame.Rect(733, 155, 35, 20),
            pygame.Rect(775, 155, 20 ,20),
            pygame.Rect(705, 185, 20, 20),
            pygame.Rect(732, 185, 35, 20),
            pygame.Rect(775, 185, 20 ,20),
            pygame.Rect(705, 215, 20, 20),
            pygame.Rect(775, 215, 20 ,20),
            pygame.Rect(605, 310, 20, 20),
            pygame.Rect(632, 310, 20, 20),
            pygame.Rect(660, 310, 20, 20),
            pygame.Rect(687, 310, 15, 80),
            pygame.Rect(605, 340, 20, 20),
            pygame.Rect(632, 340, 20, 20),
            pygame.Rect(660, 340, 20, 20),
            pygame.Rect(605, 370, 20, 20),
            pygame.Rect(632, 370, 20, 20),
            pygame.Rect(600, 507, 20, 20),
            pygame.Rect(570, 507, 20, 20),
            pygame.Rect(540, 507, 20, 20),
            pygame.Rect(510, 507, 20, 20),
            pygame.Rect(600, 532, 20, 20),
            pygame.Rect(570, 532, 20, 20),
            pygame.Rect(510, 532, 20, 20),
        ]

        self.doors = [
            pygame.Rect(92.7, 115, 15, 35),
            pygame.Rect(243, 115, 15, 35),
            pygame.Rect(248, 275, 15, 35),
            pygame.Rect(43, 265, 15, 35),
            pygame.Rect(37, 515, 15, 35),
            pygame.Rect(190, 435, 30, 30),
            pygame.Rect(308, 465, 15, 35),
            pygame.Rect(448, 170, 15, 30),
            pygame.Rect(550, 184, 15, 35),
            pygame.Rect(733, 224, 35, 35),
            pygame.Rect(663, 370, 15, 30),
            pygame.Rect(543, 532, 15, 28),
        ]

        self.knobs = [
            pygame.Rect(100, 130, 3, 3),
            pygame.Rect(251, 130, 3, 3),
            pygame.Rect(256, 290, 3, 3),
            pygame.Rect(51, 281, 3, 3),
            pygame.Rect(47, 530, 3, 3),
            pygame.Rect(210, 450, 3, 3),
            pygame.Rect(318, 480, 3, 3),
            pygame.Rect(458, 185, 3, 3),
            pygame.Rect(560, 200, 3, 3),
            pygame.Rect(755, 240, 3, 3),
            pygame.Rect(745, 240, 3, 3),
            pygame.Rect(672, 385, 3, 3),
            pygame.Rect(552, 545, 3, 3),
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
