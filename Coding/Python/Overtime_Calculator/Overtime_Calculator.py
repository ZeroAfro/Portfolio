#Program to determine overtime

#Imports
import sys


#Function to ask if they would like continue or exit
def beginning_prompt():

  while True:

    answer = input("Would you like to exit? (yes/no): ").strip().lower()

    if answer in ["yes", "y"]:
      sys.exit()

    elif answer in ["no", "n"]:
      break

    else:
      input("Please enter 'yes' or 'no': ")
      beginning_prompt()


while True:

  try:
    
    hours_worked = float(input("How many hours have you worked this week?: "))

  except ValueError:
    print("Please enter a number.")
    continue

  #Checking if the user has worked more than 40 hours or less than
  if hours_worked > 40:
    
    while True:

      try:
        hourly_wage = float(input("What is your hourly wage?: "))

        overtime_hours = float(hours_worked - 40)
        overtime_pay = float(overtime_hours *1.5 * hourly_wage)

        print(f"You have are owned ${overtime_pay:.2f} overtime pay.")
        beginning_prompt()

      except ValueError:
        print("Please enter a number.")
        continue


  elif hours_worked <= 40:
    print("You are not due any overtime pay.")
    beginning_prompt()