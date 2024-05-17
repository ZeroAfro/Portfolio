#Earnings Calculator

#user inputs into variables
employee_name = input("What is your employee's name (first and last)?: ").strip().title()
hourly_wage = input("What is your hourly wage?: ")
hours_worked = input("How many hours have your worked this current week?: ")

#turning variables into floats
hourly_wage = float(hourly_wage)
hours_worked = float(hours_worked)

#Calculating the weekly earnings
total_earnings = hours_worked * hourly_wage


#final print statement
print(f"{employee_name} earned ${total_earnings:.2f} this week.")

#input to request user input to close the code
input("Please press ENTER to exit")
