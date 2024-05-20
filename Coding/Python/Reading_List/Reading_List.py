# Reading List Program

# Library Imports
from sys import exit
import os
import random


# Setting up the absolute path for the file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(os.getcwd(), 'Reading List.txt')

# Spacing function
def space():
    print(" ")

# Exit prompt function
def exit_prompt():
    
    while True:
        answer = input("Would you like to go back to the main menu? (Y/N): ").strip().lower()
        space()
            
        if answer in ["y", "yes"]:
            break
        
        elif answer in ["n", "no"]:
            exit()
                
        else:
            space()
            print("Please enter a valid option.")
            space()
            exit_prompt()
            
# Function to allow for quicker title input            
def mass_title():
    while True:
        answer = input("More? (Y/N): ").strip().lower()
        space()
        
        if answer in ["y", "yes"]:
            break
        elif answer in ["n", "no"]:
            exit()
        else:
            space()
            print("Please enter a valid option.")
            space()

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

        if answer in ["a", "add"]:
            
            while True:
                     
                answer = input("(S)ingle/(M)ass: ").strip().lower()
                space()
            
                if answer in ["s", "single"]:
        
                    with open('Reading List.txt', 'a') as file:

                        while True:

                            title = input("What's the title?:\n").strip().title()

                            space()
                            file.write(f"[{title}]" + '\n')
                            print(f"[{title}] has been added!")
                            space()
                            break
                    break
                
                elif answer in ["m", "mass"]:
                    
                    with open('Reading List.txt', 'a') as file:
                              
                        while True:
                            
                            title = input("[Title]:\n").strip().title()
                            
                            space()    
                            file.write(f"[{title}]" + '\n')
                            mass_title()
                
                else:
                    space()
                    print("Please enter a valid option.")
                    space()
                        
        
        elif answer in ["r", "random"]:

            with open("Reading List.txt", 'r') as file:

                # Reads all lines from the file into the 'lines' variable and gets the size of the file into the 'file_size' variable 
                lines = file.readlines()
                file_size = os.path.getsize(file_path)

                # TODO: The ability to select a specific amount of random titles
                # Checks to see if the file has any content inside or not
                if (file_size == 0):
                    space()
                    print("The list is empty")
                    space()
                    exit_prompt()
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
                    exit_prompt()   
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