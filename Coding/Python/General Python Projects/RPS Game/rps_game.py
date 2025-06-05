"""
A game of rock, paper, scissors against the computer.
You can enter one of four options:
    'r' to choose rock.
    'p' to choose paper.
    's' to choose scissors
    'q' to quit the game

Your wins, losses, and ties tracked each round.
"""

import random
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

# Logging is configured for debugging. To enable debug output,
# comment out the `logging.disable()` line below.
# logging.disable()


def main() -> None:
    """
    Play a command-line Rock, Paper, Scissors game against the computer.

    The game continues in a loop, allowing the user to choose:
        rock (r), paper (p), scissors (s), or quit (q).

    After each round, the program displays the result (win, loss, or tie)
    and updates the game statistics accordingly.

    The game ends when the user inputs 'q'.

    Game statistics (wins, losses, ties) are displayed after each round.
    Debug logging is available to trace internal decisions and flow.

    Returns:
        None
    """

    # Initialize counters for game statistics.
    wins: int = 0
    losses: int = 0
    ties: int = 0

    logging.debug("--- Start of 'main()' function ---")

    print("ROCK, PAPER, SCISSORS")

    while True:
        # Display current game statistics.
        print("%s Wins, %s Losses, %s Ties\n" % (wins, losses, ties))

        # Get the player's move.
        while True:
            print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
            player_move = input(">").lower()
            logging.info(f"Payer Move: {player_move}")

            # Handle quitting the game.
            if player_move == "q":
                logging.debug("Option 'q' chosen to quit the program.")
                sys.exit()

            # Proceed only if the input is valid.
            elif player_move in ["r", "p", "s"]:
                break

            # Prompt again if input is invalid.
            else:
                logging.warning(f"User entered invalid input: {player_move}")
                print(
                    "\nPlease enter a valid option of: (r) (p) (s) or (q)...\n"
                )

        # Print the player's chosen move.
        if player_move == "r":
            print("\nROCK versus...")
        elif player_move == "p":
            print("\nPAPER versus...")
        elif player_move == "s":
            print("\nSCISSORS versus...")

        # Randomly select the comptuter's move.
        move_number = random.randint(1, 3)
        logging.info(f"Move Number: {move_number}")

        # Determine the outcome of the round.
        if move_number == 1:
            computer_move = "r"
            print("ROCK\n")
        elif move_number == 2:
            computer_move = "p"
            print("PAPER\n")
        elif move_number == 3:
            computer_move = "s"
            print("SCISSORS\n")

        if player_move == computer_move:
            print("It was a tie!\n")
            ties += 1
        elif player_move == "r" and computer_move == "s":
            print("You win!\n")
            wins += 1
        elif player_move == "p" and computer_move == "r":
            print("You win!\n")
            wins += 1
        elif player_move == "s" and computer_move == "p":
            print("You win!\n")
            wins += 1
        elif player_move == "r" and computer_move == "p":
            print("You lose!\n")
            losses += 1
        elif player_move == "p" and computer_move == "s":
            print("You lose!\n")
            losses += 1
        elif player_move == "s" and computer_move == "r":
            print("You lose!\n")
            losses += 1

        logging.debug("--- End of 'main()' function ---")


if __name__ == "__main__":
    main()
