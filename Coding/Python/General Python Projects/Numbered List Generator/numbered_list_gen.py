"""
Generates a numbered and formated empty list based on user input.
"""

from sys import exit

path = "numbered_list.txt"

print(
    "\nWelcome to the numbered list generator\n\n"
    "Please enter how long you wish the list to be or "
    "enter 'q' to quit.\n\n"
    )

while True:
    list_length = input("List Length: ")

    if list_length.lower() == "q":
        exit()
    else:
        try:
            list_length = int(list_length)
            break
        except ValueError:
            print("\nPlease enter either whole number or 'q'.\n")

open(path, "w").close()

with open(path, "a") as file:

    for n in range(1, list_length + 1):

        formated_list = f"{n}: \n"

        if n == list_length:
            formated_list = f"{n}: "
            file.write(formated_list)
        else:
            file.write(formated_list)
