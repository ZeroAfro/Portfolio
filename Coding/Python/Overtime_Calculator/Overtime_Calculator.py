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

  hours_worked = float(input("How many hours have you worked this week?: "))
  
  #Checking if the user has worked more than 40 hours or less than
  if hours_worked > 40:

    hourly_wage = float(input("What is your hourly wage?: "))

    hours_worked = float((hours_worked - 40) * 1.5)
    print(f"You have are owned ${hours_worked:.2f} overtime pay.")

    beginning_prompt()

  elif hours_worked < 40:
    print("You are not due any overtime pay.")
    beginning_prompt()