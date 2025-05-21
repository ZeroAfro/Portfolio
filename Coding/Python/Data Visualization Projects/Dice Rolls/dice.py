"""Dice class simulation"""

from random import randint


class Die:
    """Simulates a 6 sided die"""

    def __init__(self, num_sides: int = 6):
        self.num_sides: int = num_sides

    def roll(self) -> int:
        """Returns a random value between 1 and the number of sides"""

        return randint(1, self.num_sides)
