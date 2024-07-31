"""Dice class simulation"""

from random import randint


class Die:
    """Simulates a 6 sided die"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Returns a random value between 1 and the number of sides"""

        return randint(1, self.num_sides)
