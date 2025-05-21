from random import choice


class RandomWalk:
    """Class to generate random 2D walks."""

    def __init__(self, num_points: int = 5000):
        """Initializes attributes of a walk"""

        self.num_points: int = num_points
        self.x_values: list[int] = [0]
        self.y_values: list[int] = [0]

    def get_step(self) -> int:
        """Calculates a single step in a random direction."""

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

    def fill_walk(self) -> None:
        """Calculate all the points in the walk"""

        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
