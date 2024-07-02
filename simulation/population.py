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
        self.peak_incubating = 0

    def infected_random_people(self):
        random_people = random.choice(self.people)
        random_people.infect()

    def get_infected_count(self):
        return sum(1 for person in self.people if person.is_infected())

    def get_incubation_count(self):
        return sum(1 for person in self.people if person.is_incubating())

    def get_health_count(self):
        return sum(1 for person in self.people if person.health_status == 'healthy')

    def update(self):
        incubating_count = self.get_incubation_count()
        infected_count = self.get_infected_count()

        if incubating_count > self.peak_incubating:
            self.peak_incubating = incubating_count

        for person in self.people:
            person.move()
            for other_person in self.people:
                if person != other_person and person.rect.colliderect(other_person):
                    person.contact_with(other_person)
                    other_person.contact_with(person)
            person.update_health_status()

    def draw(self, screen):
        for person in self.people:
            person.draw(screen)
