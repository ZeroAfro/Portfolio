"""
wage_calculator.py

This script calculates regular and overtime wages based on the user's
hourly pay rate and hours worked.

It follows the federal definition of overtime: any hours worked over 40
in a workweek is considered overtime and are paid at 1.5 times the
regular rate of pay.
"""

from sys import exit


def calculate_wage(hourly_rate: float, hours_worked: float) -> float:
    """
    Calculates either the regular wage or the overtime wage and total wage
    based on how many hours the user inputs.

    40 hours or less: Regular Wage is calculated and returned

    over 40 hours: Overtime wage and total wage is calculated
    and returned.
    """

    if hours_worked <= 40:
        regular_wage = hours_worked * hourly_rate
        return regular_wage
    elif hours_worked > 40:
        regular_wage = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_rate = hourly_rate * 1.5
        overtime_wage = overtime_hours * overtime_rate
        total_wage = regular_wage + overtime_wage
        return overtime_wage, total_wage


def main():
    """
    Interacts with the user to calculate wages.

    Prompts the user for hours worked and hourly rate, then displays the
    regular or overtime wage based on the input. The user can quit by
    entering 'q'.

    Calls the 'calculate_wage' function to compute the wage.
    """

    text = "Welcome to wage_calculator.py!"
    width = len(text)

    print("*" * (width + 4))
    print(f"* {text} *")
    print("*" * (width + 4))

    print("\nPlease enter the total hours worked and the hourly "
          "wage to get started.")
    print("You can quit anyime by entering 'q'\n")

    while True:
        try:
            hours_input = input("Total Hours Worked: ").strip()
            if hours_input.lower() == 'q':
                exit()
            hours_worked = float(hours_input)
            break
        except ValueError:
            print("\nPlease enter a valid numerical value.\n\n")

    while True:
        try:
            rate_input = input("Hourly Pay Rate: ").strip()
            if rate_input.lower() == 'q':
                exit()
            hourly_rate = float(rate_input)
            break
        except ValueError:
            print("\nPlease enter a valid numerical value.\n\n")

    if hours_worked <= 40:
        regular_wage = calculate_wage(hourly_rate, hours_worked)

        print(f"\n\n\033[1mHours Worked\033[0m: {hours_worked}")
        print(f"\033[1mHourly Pay Rate\033[0m: ${hourly_rate}")
        print(f"\033[1mTotal wages\033[0m: ${regular_wage:.2f}\n\n")
        input("Press 'ENTER' to close...")
        exit()
    elif hours_worked > 40:
        overtime_wage, total_wage = calculate_wage(hourly_rate, hours_worked)
        print(f"\n\n\033[1mHours Worked\033[0m: {hours_worked}")
        print(f"\033[1mHourly Pay Rate\033[0m: ${hourly_rate}")
        print(f"\033[1mOvertime Wage\033[0m: ${overtime_wage:.2f}")
        print(f"\033[1mTotal Wages\033[0m: ${total_wage:.2f}\n\n")


if __name__ == "__main__":
    main()
