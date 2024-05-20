#Reading List project

#Imports
import sys
import os
import random


#Setting up the absolute path for the txt list
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(os.getcwd(), "Reading List.txt")

def continuation_prompt():
    
    while True:
        answer = input("Would you like to go back to the main menu? (Y/N): ").strip().lower()
            
        if answer in ["y", "yes"]:
            break
        
        elif answer in ["n", "no"]:
            sys.exit()
                
        else:
            print("Please enter a valid option.")
            continuation_prompt()

while True:
        
        answer = input("Please select a option (A)dd/(R)andom? or type 'delete now' to delete list: ").strip().lower()
    
        if answer in ["a", "add"]:
        
            with open("Reading List.txt",'a') as file:

                answer = input("Please add the title of the story you wish to add to the list:\n").strip().title()
            
                file.write(f"[{answer}]" + '\n')

                print("<Title is now saved>")

            continuation_prompt()
        
        elif answer in ["r", "random"]:

            with open("Reading List.txt", 'r') as file:

                #using Random library to pull a random title out of the txt list
                lines = file.readlines()
                choice = random.choice(lines).strip()

                print(choice)

            continuation_prompt

        elif answer == "delete now":
                    
            open("Reading List.txt", "w").close()

            print("List has been deleted!")
            continuation_prompt()   

        else:
            print("Please select a valid entry.")
            continuation_prompt