#Earnings Calculator

# User inputs into variables
employee_name = input("What is your employee's name (first and last)?: ").strip().title()
hourly_wage = input("What is your hourly wage?: ")
hours_worked = input("How many hours have your worked this current week?: ")

# Turns variables into float values
hourly_wage = float(hourly_wage)
hours_worked = float(hours_worked)

# Calculating the earnings
total_earnings = hours_worked * hourly_wage

print(f"{employee_name} earned ${total_earnings:.2f} this week.")

# Input to request user input to close the code
input("Please press ENTER to exit")
