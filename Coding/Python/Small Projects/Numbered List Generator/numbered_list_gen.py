# Numbered List Generator
# TODO: Figure out why I have to use os.chdir to ensure file creation

import os
from time import sleep

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    try:
        list_length = int(input("Enter the length of the numbered list: "))
        break
    except ValueError:
        print("Please enter a valid number.")

with open("numbered_list.txt", "w") as file:
    i = 0
    while i < list_length:
        i += 1
        file.write(f"{i}. \n")

delay_time = 1
print(f"Closing in {delay_time} seconds...")
sleep(delay_time)
