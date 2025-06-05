"""
guessTheNumber.py is a number-guessing game.

Within four guesses you must find the secret number, an integer between 1 and
20.

Rules:
    1. You have four guesses.
    2. After each guess you are told if it was too high or too low.
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


def main() -> None:
    """
    Main function to run the number guessing game.

    The player has four attempts to guess a randomly chosen
    number between 1 and 20. After each guess, feedback is
    given whether the guess was too high or too low.
    """

    logging.debug("--- Start of 'main()' function ---")

    # Store the user's valid guesses
    guesses: list[int] = []

    # Generate the secret number between 1 and 20
    secret_number: int = random.randint(1, 20)
    logging.info("The secret number generated: %s", secret_number)

    print("I'm thinking of a number between 1 and 20...")
    print("You have four chances to guess it!\n")

    # Loop for a maximum of 4 guesses
    for _guesses_taken in range(1, 5):

        # Continuously prompt until a valid guess (1-20) is entered
        while True:
            try:
                print("Take a guess:")
                user_input = input(">")
                guess = int(user_input)

            except ValueError:
                logging.warning("User entered invalid input: %s", user_input)
                print("\nPlease enter a valid number...\n")
                continue

            if guess < 1 or guess > 20:
                logging.warning(
                    "User entered a value that is not 1-20: %s", guess
                )
                print("\nYour guess must be between 1 and 20.\n")
            else:
                break

        logging.info("User Input: %s", guess)
        guesses.append(guess)
        logging.info("Guess %s added to list.", guess)

        if guess < secret_number:
            print("\nYour guess is too low.\n")
        elif guess > secret_number:
            print("\nYour guess is too high.\n")
        else:
            break

    # Determine and report final result to the user
    if guess == secret_number:
        print(
            f"\nYou guessed it! You got it in {str(len(guesses))} guesses!\n"
        )
        logging.info(
            "User guessed the secret number in %s guesses.", len(guesses)
        )
    else:
        print(f"Sorry you didn't win! The correct number was: {secret_number}")
        logging.info(
            "User failed to guess the secret number within four guesses."
        )

    logging.debug("--- End of 'main()' function ---")


if __name__ == "__main__":
    main()
