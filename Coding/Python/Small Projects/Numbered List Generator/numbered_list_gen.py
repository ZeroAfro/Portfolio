# Numbered List Generator
# TODO: Change os file path to just current directory and include code to make it create text file if none exist

# Library Imports
import os
from time import sleep

# Changes working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Checks for valid user input
while True:
    try:
        list_length = int(input("Enter the length of the numbered list: "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Openning the file in write mode and executing while loop
with open('numbered_list.txt','w') as file:
    i = 0
    while i < list_length:
        i += 1
        file.write(f"{i}. \n")

# Program will stay open for 1 second before closing
delay_time = 1
print(f"Closing in {delay_time} seconds...")
sleep(delay_time)
