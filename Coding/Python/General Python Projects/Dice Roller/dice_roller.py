"""Random Dice Roller"""

from random import randint


def goodbye_prompt():
    """Prints goodbye and sets active to False to end loop"""

    global active
    print("\nGoobye!\n")
    active = False


class Dice:
    """Model of a dice"""

    def __init__(self, side):
        self.side = side
        self.roll_amount = 0

    def single_roll(self):
        """Rolls the dice a single time"""

        dice = randint(1, self.side)
        self.roll_amount += 1
        print(f"\n\t{dice}\n")

    def multi_roll(self, rolls):
        """Rolls the dice multiple times"""

        print("\n")
        for dice in range(rolls):
            dice = randint(1, self.side)
            self.roll_amount += 1
            print(f"\t{dice}")
        print("\n")

    def roll_count(self):
        """Returns message about how many times you have rolled the dice"""

        print(f"\n\tYou have rolled the dice {self.roll_amount} times.\n")

    def reset_rolls(self):
        """Resets roll count"""

        self.roll_amount = 0


active = True
dice = None

prompt = "Please enter 'quit' at anytime to exit."
print(prompt)

while active:
    print(
        "Which of the following would you like to do?\n"
        "\t-Single Dice Roll(single)\n"
        "\t-Multi Dice Roll(multi)\n"
        "\t-Check Roll Count(count)\n"
        "\t-Reset Roll Count(reset)\n"
    )
    answer = input("").strip().lower()

    while True:
        if answer == "single":
            dice_sides = input("How many sides does your dice have?: ")

            if dice_sides.isdigit():
                dice_sides = int(dice_sides)
                dice = Dice(dice_sides)
                dice.single_roll()
                break
            elif dice_sides == "quit":
                goodbye_prompt()
                break
            else:
                print("Please enter a valid number.")

        elif answer == "multi":
            dice_sides = input("How many sides does your dice have?: ")

            if dice_sides == "quit":
                goodbye_prompt()
                break
            rolls = input("How many times would you like to roll the dice?: ")
            if rolls == "quit":
                goodbye_prompt()
                break
            if dice_sides.isdigit() and rolls.isdigit():
                dice_sides = int(dice_sides)
                rolls = int(rolls)
                dice = Dice(dice_sides)
                dice.multi_roll(rolls)
                break
            else:
                print("Please answer valid numbers for the options.")

        elif answer == "count":
            if dice:
                Dice.roll_count(dice)
                break
            else:
                print("\t\nYou havent rolled the dice yet.\n")
                break

        elif answer == "reset":
            Dice.reset_rolls(dice)
            print("\n\tRoll count is reset!\n")
            break

        elif answer == "quit":
            goodbye_prompt()
            break
