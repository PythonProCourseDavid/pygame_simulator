import pygame
import psycopg2
from datetime import datetime

from simulation import Population

START_TIME = 0
END_TIME = 0
TOTAL_INFECTED_TIME = 0
AVG_INFECTION_TIME = 0
P30_TIME = 0
P50_TIME = 0
P70_TIME = 0
PEAK_INCUBATING = 0
SUM_OF_POPULATION = 0

DB_NAME = 'postgres'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'


class Statistics:
    def __init__(self):
        self.start_time = START_TIME
        self.end_time = END_TIME
        self.total_infected_time = TOTAL_INFECTED_TIME
        self.avg_infected_time = AVG_INFECTION_TIME
        self.p30_time = P30_TIME
        self.p50_time = P50_TIME
        self.p70_time = P70_TIME
        self.peak_incubating = PEAK_INCUBATING
        self.game_date = datetime.now()
        self.sum_of_population = SUM_OF_POPULATION

    def start_time(self):
        self.start_time = pygame.time.get_ticks()

    def format_date(self):
        current_date = self.game_date.strftime('%Y-%m-%d')
        current_time = self.game_date.strftime('%H:%M:%S')
        return current_date, current_time


