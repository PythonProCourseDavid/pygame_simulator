import random


class ProbabilityCalculation:
    @staticmethod
    def infect_probability(distance, health_status):
        base_prob = random.random()

        if distance < 20:
            base_prob *= 2

        if health_status == 'infected':
            base_prob *= 3

        return base_prob < 0.5

    @staticmethod
    def incubation_probability():
        return random.random() < 0.5
