import random

from .person import Person

NUMS_OF_PERSONS = 50


class Population:
    def __init__(self, width, height, city):
        self.width = width
        self.height = height
        self.city = city
        self.people = [Person(width, height, city) for _ in range(NUMS_OF_PERSONS)]
        self.infected_random_people()

    def infected_random_people(self):
        random_people = random.choice(self.people)
        random_people.infect()

