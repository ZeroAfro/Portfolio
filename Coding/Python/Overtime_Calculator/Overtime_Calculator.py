# Overtime Wage Calculator

# Library Imports
from sys import exit


# Function to ask if they would like to exit
def exit_prompt():

  while True:

    answer = input("Would you like to exit? (yes/no): ").strip().lower()

    if answer in ["yes", "y"]:
      exit()

    elif answer in ["no", "n"]:
      break

    else:
      input("Please enter 'yes' or 'no': ")
      exit_prompt()


while True:

  try:
    
    hours_worked = float(input("How many hours have you worked this week?: "))

  except ValueError:
    print("Please enter a number.")
    continue

  # Checking if the user has worked more or less than 40 hours
  if hours_worked > 40:
    
    while True:

      try:
        hourly_wage = float(input("What is your hourly wage?: "))

        overtime_hours = float(hours_worked - 40)
        overtime_pay = float(overtime_hours *1.5 * hourly_wage)

        print(f"You have are owned ${overtime_pay:.2f} overtime pay.")
        exit_prompt()

      except ValueError:
        print("Please enter a number.")
        continue


  elif hours_worked <= 40:
    print("You are not due any overtime pay.")
    exit_prompt()
    
  else:
    print("Please enter a valid number.")