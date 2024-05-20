# Reading List Program

# Library Imports
from sys import exit
import os
import random


# Setting up the absolute path for the txt list
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(os.getcwd(), "Reading List.txt")

# Function to add spacing 
def space():
    print(" ")

# Function for situations where I don't want to immediatly bring the user back to the main menu
def continuation_prompt():
    
    while True:
        answer = input("Would you like to go back to the main menu? (Y/N): ").strip().lower()
            
        if answer in ["y", "yes"]:
            break
        
        elif answer in ["n", "no"]:
            exit()
                
        else:
            print("Please enter a valid option.")
            continuation_prompt()


while True:
        
        print("[Options:]")
        print(" ")
        print("(A)dd")
        print("(R)andom")
        print("(D)elete")
        print("(E)xit")
        space()

        answer = input("Please enter one of the above options: ").strip().lower()
        space()


        # TODO: Add the ability to enter a "mass title" mode which will let you enter titles after title without any prompts
        if answer in ["a", "add"]:
        
            with open("Reading List.txt",'a') as file:

                while True:

                    answer = input("Please add the title of the story you wish to add to the list:\n").strip().title()

                    space()
                    file.write(f"[{answer}]" + '\n')
                    print("<Title is now saved>")
                    space()

                    answer = input("Would you like to enter more titles (Y/N): ").strip().lower()
                    space()

                    if answer in ["y", "yes"]:
                        print(" ")
                        continue
                    elif answer in ["n", "no"]:
                       space()
                       break
                    else:
                        print("Please enter a valid option.")
                        space()
        
        elif answer in ["r", "random"]:

            with open("Reading List.txt", 'r') as file:

                # Read all lines from the file into the 'lines' variable and get the size of the file into the 'file_size' variable 
                lines = file.readlines()
                file_size = os.path.getsize(file_path)

                # TODO: The ability to select a specific amount of random titles
                
                # Checks to see if the file has any content inside or not
                if (file_size == 0):
                    space()
                    print("The list is empty")
                    space()
                    continuation_prompt()
                    space()
                elif (file_size > 0):
                    choice = random.choice(lines).strip()
                    space()
                    print(f"<{choice}>")
                    space()
                    continue
                else:
                    space()
                    print("An unknown error has occured.")
                    space()
                    continue

        elif answer in ["d", "delete"]:

            while True:

                answer = input("Are you sure? Please type 'Delete Now' to confirm or '(E)xit for the main menu: ").strip().title()
                space()

                if answer == "Delete Now":    
                    open("Reading List.txt", "w").close()
                    space()
                    print("List has been deleted!")
                    space()
                    continuation_prompt()   
                elif answer in ["E", "Exit"]:
                    space()
                    break
                else:
                    space()
                    print("Please enter a valid option.")
                    space()
        elif answer in ["e", "exit"]:
            exit()

        else:
            space()
            print("Please enter a valid option.")
            space()