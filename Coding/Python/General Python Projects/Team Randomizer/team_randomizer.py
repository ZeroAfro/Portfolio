"""
Generates random teams of two players each from a fixed list,
ensuring that no team is repeated twice in a row.

Intended for use in quick team randomization scenarios,
with console input to generate new teams interactively.
"""

import random
import logging

FRIENDS: list[str] = ["friend1", "friend2", "friend3", "friend4"]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Logging is configured for debugging. To enable debug output,
# comment out the `logging.disable()` line below.
logging.disable()


def team_randomizer() -> tuple[list[str], list[str]]:
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

    # List of players to choose from
    friends = FRIENDS.copy()

    # Select four unique players by choosing and removing one at a time
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


def main() -> None:
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

    # Keep track of teams generated in the previous round
    # as sets for easy comparison
    previous_teams: list[set[str]] = []

    # Run indefinitely until the user manually stops,
    # generating new teams on ENTER
    while True:
        logging.debug("--- Start of main while loop ---")
        input("\nPress 'ENTER' to generate teams...\n")

        logging.debug("Called 'team_randomizer()'")
        team_1, team_2 = team_randomizer()

        # Ensure newly generated teams are different from the previous teams
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
                # Keep regenerating teams until both teams differ from
                # the previous round
                logging.debug("Called 'team_randomizer()'")
                team_1, team_2 = team_randomizer()
                logging.debug(
                    f"Trying new teams: Team 1 - {sorted(team_1)}, "
                    f"Team 2 - {sorted(team_2)}"
                )

            # Use sets to ignore order when comparing teams
            previous_teams = [set(team_1), set(team_2)]
            logging.debug("End of 'IF' statement.")

        else:
            logging.debug("Start of 'ELSE' statement.")

            # Use sets to ignore order when comparing teams
            previous_teams = [set(team_1), set(team_2)]
            logging.debug("End of 'ELSE' statement.")

        print(f"Team 1: {' and '.join(sorted(team_1))}")
        print(f"Team 2: {' and '.join(sorted(team_2))}")

        logging.info(
            f"Teams generated: Team 1 - {sorted(team_1)}, "
            f"Team 2 - {sorted(team_2)}"
        )

        logging.debug("--- End of main while loop ---")


if __name__ == "__main__":
    main()
