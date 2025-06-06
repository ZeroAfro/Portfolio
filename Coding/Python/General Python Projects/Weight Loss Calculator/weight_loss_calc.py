"""
Weight loss calculator.

Collects weekly Total Daily Energy Expenditure (TDEE) inputs from the user,
validates them, and calculates the average daily caloric intake required
to lose either 1 or 2 pounds per week.

Logs key events and warns on invalid input. Outputs the final caloric
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
    Main program function to run the weight loss calculator.

    Prompts the user to:
    - Specify the number of weeks to calculate (minimum two weeks).
    - Choose a weight loss goal of 1 or 2 pounds per week.
    - Enter weekly TDEE values.

    Validates all inputs and logs relevant information and warnings.

    Calculates the average TDEE and subtracts the appropriate daily caloric
    deficit (500 calories for 1 pound/week, 1000 for 2 pounds/week) to
    determine the recommended daily caloric intake.

    Prints the final caloric recommendation.

    The user can quit the program anytime by entering 'q'.
    """

    weekly_tdees: list[int] = []

    logging.debug("--- Start of 'main()' ---")

    print(
        """
        Welcome to the weight loss calculator.

        Please note that this is not meant to replace
        medical advice. This is simply a tool to help to
        find a general estimation of your caloric deficit.

        Before starting any diet you should always check
        with a doctor or other professional.

        I made this in order to help me keep track of my
        goals during my weightloss journey.

        Always check any info given with a professional.

        You can exit anytime by entering 'q'...\n
        """
    )

    # Prompt user to enter how many weeks they wish to calculate.
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

    # Prompt user to enter rather they want to lose one or two pounds a week.
    while True:
        print("How many pounds per week would you like to lose? Enter 1 or 2.")
        user_pounds = input(">").strip()
        if user_pounds.lower() == "q":
            sys.exit()

        try:
            pounds_lost = int(user_pounds)
        except ValueError:
            logging.warning(
                "User entered a non-integer value for pounds: %s", user_pounds
            )
            print("Please enter a valid number of either '1' or '2'...\n")
            continue

        if pounds_lost not in (1, 2):
            logging.warning(
                "User entered %s; must be either be " "'1' or '2'", pounds_lost
            )
            print("Must enter either '1' or '2' pounds...\n")
            continue

        # Set daily caloric deficit based on pounds lost per week goal.
        target_deficit = 500 if pounds_lost == 1 else 1000
        logging.info(
            "User selected to lose %s pounds per week. Target daily deficit "
            "set to %s calories",
            pounds_lost,
            target_deficit,
        )
        break

    # Prompt user to enter TDEE values for each week.
    for _ in range(0, total_weeks):
        while True:
            print("Please enter your TDEE value:")
            user_input = input(">").strip()
            if user_input.lower() == "q":
                sys.exit()

            try:
                tdee_value = int(user_input)
                if tdee_value == 0:
                    logging.warning("User entered zero as the integer value.")
                    print("Your TDEE cannot be zero.\n")
                    continue
                elif tdee_value < 0:
                    logging.warning("User entered a negative integer value.")
                    print(
                        "You entered a negative number, your TDEE cannot "
                        "be negative.\n"
                    )
                    continue
            except ValueError:
                logging.warning(
                    "User entered a non-integer value for TDEE: %s", user_input
                )
                print("Please enter a valid number...\n")
                continue

            # Append valid TDEE to the list.
            weekly_tdees.append(tdee_value)
            break

    logging.debug("TDEE values: %s", weekly_tdees)
    weekly_sum = sum(weekly_tdees)
    logging.info("Sum of weekly TDEE values: %s", weekly_sum)
    # Calculates the average TDEE from the list of weekly values.
    weekly_average = weekly_sum // len(weekly_tdees)
    logging.info("%s / %s = %s", weekly_sum, len(weekly_tdees), weekly_average)
    # Calculates caloric deficit by taking the average and subtracting either
    # 500 for one pound or 1000 for two pounds.
    # TODO: Prevent negative caloric deficit values
    caloric_deficit = weekly_average - target_deficit
    logging.info("%s - %s = %s", weekly_average, pounds_lost, caloric_deficit)

    if caloric_deficit < 1200:
        logging.info(
            "User's calculated caloric deficit is %s a day; this is under "
            "the medically safe minimum of 1200 calories a day",
            caloric_deficit,
        )
        print(
            "\n---Anything less than 1,200 calories a day isn't recommended "
            "without doctor supervision.---\n"
        )

    print(
        f"\tTo lose {user_pounds} pound(s) a week you'll need to "
        f"eat {caloric_deficit} calories a day.\n"
    )
    logging.debug("--- End of 'main()' ---")
    input("Press 'ENTER' to exit...")
    sys.exit()


if __name__ == "__main__":
    main()
