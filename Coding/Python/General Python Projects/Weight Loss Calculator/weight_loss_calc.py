"""
Collects weekly TDEE inputs from the user, validates them, and calculates
an average daily caloric intake needed to lose 2 pounds per week.

Logs key steps and warns on invalid input. Outputs the final caloric
recommendation.
"""

import logging
import sys

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
    Prompt for weekly TDEE values, validate input, and compute average TDEE.

    Calculate daily calories to lose 2 pounds/week by subtracting 1000
    from the average. User can quit anytime with 'q'.

    Logs key steps and prints the final recommendation.

    Note: Negative caloric intake values are not handled.
    """

    weekly_tdees: list[int] = []

    logging.debug("--- Start of 'main()' ---")

    print("Welcome to the weight loss calculator...")
    print("You can enter 'q' to quit at any time\n")

    while True:
        print("How many weeks do you want to calculate?")
        user_weeks = input(">").strip()
        if user_weeks.lower() == "q":
            sys.exit()
        try:
            total_weeks = int(user_weeks)
        except ValueError:
            logging.warning(
                "User entered a non-integer value for weeks: %s", user_weeks
            )
            print("Please enter a valid number...\n")
            continue
        if total_weeks <= 1:
            logging.warning(
                "User entered %s weeks; must enter at least two weeks.",
                total_weeks,
            )
            print("Must enter at least two weeks.\n")
            continue

        break

    # Prompt user to enter TDEE values for each week.
    for _weeks in range(0, total_weeks):
        while True:
            print("Please enter your TDEE value:")
            user_input = input(">").strip()
            if user_input.lower() == "q":
                sys.exit()
            try:
                tdee_value = int(user_input)
                if tdee_value <= 0:
                    if tdee_value == 0:
                        logging.warning(
                            "User entered zero as the integer value."
                        )
                        print("Your TDEE cannot be zero.\n")
                        continue
                    else:
                        logging.warning(
                            "User entered a negative integer value."
                        )
                        print(
                            "You entered a negative number, your TDEE "
                            "cannot be negative.\n"
                        )
                        continue
            except ValueError:
                logging.warning(
                    "User entered a non-integer value for TDEE: %s", user_input
                )
                print("Please enter a valid number...\n")
                continue

            # Adds each TDEE as a list value to 'weekly_tdees'.
            weekly_tdees.append(tdee_value)
            break

    logging.debug("TDEE values: %s", weekly_tdees)
    weekly_sum = sum(weekly_tdees)
    logging.info("Sum of weekly TDEE values: %s", weekly_sum)
    # Calculates the average TDEE from the list of weekly values.
    weekly_average = weekly_sum // len(weekly_tdees)
    logging.info("%s / %s = %s", weekly_sum, len(weekly_tdees), weekly_average)
    # Calculates caloric deficit by taking the average and subtracting 1000.
    # TODO: Prevent negative caloric deficit values
    caloric_deficit = weekly_average - 1000
    logging.info("%s - 1000 = %s", weekly_average, caloric_deficit)

    print(
        "To lose two pounds a week you need to "
        f"eat {caloric_deficit} calories a day."
    )

    logging.debug("--- End of 'main()' ---")


if __name__ == "__main__":
    main()
