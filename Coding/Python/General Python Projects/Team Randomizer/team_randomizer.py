"""
Generates random teams while making sure that
no team gets pulled twice in a row.
"""

import random
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Logging is configured for debugging. To enable debug output,
# comment out the `logging.disable()` line below.
logging.disable()


def team_randomizer() -> tuple[str, str]:
    """
    Randomly generates two teams of two players each from a predefined list.

    Selects four unique names from the 'friends' list using random choice,
    assigns the first two to Team 1 and the next two to Team 2,
    and returns both teams.

    Returns:
        tuple[list[str], list[str]]: Two teams,
            each as a list of two player names.
    """

    logging.debug("--- Start of 'team_randomizer()' function ---")

    friends: list[str] = ["Toxic", "Ryan", "Josh", "Wolf"]

    person_1 = random.choice(friends)
    friends.remove(person_1)
    person_2 = random.choice(friends)
    friends.remove(person_2)
    person_3 = random.choice(friends)
    friends.remove(person_3)
    person_4 = random.choice(friends)
    friends.remove(person_4)

    team_1 = [person_1, person_2]
    team_2 = [person_3, person_4]

    logging.debug("--- End of 'team_randomizer()' function ---")

    return team_1, team_2


def main():
    """
    Continuously generates random teams, ensuring that no
    team is repeated consecutively.

    On each ENTER key press, two teams are generated using 'team_randomizer()'.
    If either of the new teams matches one from the previous round,
    new teams are generated until both are different.
    The final teams are printed and stored for comparison.

    This function runs indefinitely until manually stopped by the user.
    """

    logging.debug("--- Start of 'main()' function ---")

    # Stores previously selected teams; each team is a list of player names.
    previous_teams: list[list[str]] = []

    while True:
        logging.debug("--- Start of main while loop ---")
        input("\nPress 'ENTER' to generate teams...\n")

        team_1, team_2 = team_randomizer()

        if set(team_1) in previous_teams or set(team_2) in previous_teams:
            logging.debug("Start of 'IF' statement.")
            logging.debug(
                f"Duplicate team detected. "
                f"Previous teams: Team 1 - {sorted(previous_teams[0])}, "
                f"Team 2 - {sorted(previous_teams[1])}"
            )

            while (
                set(team_1) in previous_teams or set(team_2) in previous_teams
            ):
                logging.debug("'team_randomizer()' called.")
                team_1, team_2 = team_randomizer()
                logging.debug(
                    f"Trying new teams: Team 1 - {sorted(team_1)}, "
                    f"Team 2 - {sorted(team_2)}"
                )
            previous_teams = [set(team_1), set(team_2)]
            logging.debug("End of 'IF' statement.")

        else:
            logging.debug("Start of 'ELSE' statement.")
            previous_teams = [set(team_1), set(team_2)]
            logging.debug("End of 'ELSE' statement.")

        print(f"Team 1: {" and ".join(sorted(team_1))}")
        print(f"Team 2: {" and ".join(sorted(team_2))}")

        logging.info(
            f"Teams generated: Team 1 - {sorted(team_1)}, "
            f"Team 2 - {sorted(team_2)}"
        )

        logging.debug("--- End of main while loop ---")


if __name__ == "__main__":
    main()
