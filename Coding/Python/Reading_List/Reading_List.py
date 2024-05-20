#Reading List project

#Imports
import sys
import os

#Absolute path to the Reading List.txt
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(os.getcwd(), "Reading List.txt")

#Function that will ask users if they wish to enter more titles or exit the program
def continuation_prompt():
    
    while True:
        answer = input("Would you like to add another title? (Y/N): ").strip().lower()
            
        if answer in ["y", "yes"]:
            break
        
        elif answer in ["n", "n"]:
            sys.exit()
                
        else:
            print("Please enter a valid option.")
            continuation_prompt()
            

while True:

    with open("Reading List.txt",'a') as file:
        
        answer = input("Please add the title of the story you wish to add to your 'Reading List' list:\n")

        #Takes the answer variable which stores the title you wish to add to the list and writes it on a new line in the txt file
        file.write(f"[{answer}]" + '\n')
        
        print("<Title is now saved>")
        
        file.close()
        continuation_prompt()
