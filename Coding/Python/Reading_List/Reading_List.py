#Reading List project

#Imports
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(os.getcwd(), "Reading List.txt")

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
            
        file.write(f"[{answer}]" + '\n')
        
        print("<Title is now saved>")
        
        file.close()
        continuation_prompt()