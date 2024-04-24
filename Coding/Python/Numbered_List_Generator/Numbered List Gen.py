import os
import time

#Changes working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#While loop to ask and check for valid user input
while True:
    try:
        list_length = int(input("Enter the length of the numbered list: "))
        break
    except ValueError:
        print("Please enter a valid number.")

#Openning text file in write mode and executing while loop
with open('numbered_list.txt','w') as file:
    i = 0
    while i < list_length:
        i += 1
        file.write(f"{i}. \n")

#Will cause the program to stay open and close after specified seconds
delay_time = 1
print(f"Closing in {delay_time} seconds...")
time.sleep(delay_time)