# Wage Calculator

# TODO: Add exit confirmations and statements

from sys import exit

# Function to add spacing
def space():
    print(" ")
    
# Start of code
print("Welcome to the wage calcuator!")
space()

while True:

    answer = input("Would you like to calculate (R)egular/(O)vertime/(E)xit: ").strip().lower()
    space()

    while True: 

        if answer in ["r", "regular"]:

            try:            
                hours_worked = float(input("How many hours did you work?: "))
                space()

                while True:
                    try:
                        hourly_wage = float(input("What's your hourly wage?: "))
                        break
                    except ValueError:
                        space()
                        print("Please enter a valid number.")
                        space()

                earnings = hours_worked * hourly_wage

                space()
                print(f"You earned: ${earnings:.2f}")
                space()
                break

            except ValueError:
                space()
                print("Please enter a valid number.")
                space()


        elif answer in ["o", "overtime"]:

            try:
                hours_worked = float(input("How many hours did you work?: "))
                space()

                if hours_worked > 40:

                    while True:

                        try:           

                            hourly_wage = float(input("What's your hourly wage?: "))
                            space()
                            break

                        except ValueError:
                            space()
                            print("Please enter a valid number.")
                            space()

                    overtime_hours = float(hours_worked - 40)
                    overtime_pay = float(overtime_hours * 1.5 * hourly_wage)

                    print(f"You earned: ${overtime_pay:.2f} in overtime.")
                    space()
                    break

                elif hours_worked <= 40:
                    print("Overtime not earned.")
                    space()
                    break

                else:
                    print("Please entera valid number.")
                    space()
            except ValueError:
                space()
                print("Please enter a valid number.")
                space()
                
        elif answer in ["e", "exit"]:
            exit()
            
        else:
            print("Please enter a valid option")
            space()
