"""
A simple death counter that can track and reset your deaths in video games
"""

import tkinter as tk


with open("counter.txt", "r") as file:
    death_count = int(file.read().strip())


def reset_count():
    """Resets death counter"""

    global death_count
    death_count = 0
    with open("counter.txt", "r+") as file:
        file.truncate()
        file.write("0")
        count_display.config(text=f"{death_count}", font=("Helvetica", 25))


def increase_count():
    """Incraments death counter"""

    global death_count
    with open("counter.txt", "r+") as file:
        death_count += 1
        count_display.config(text=f"{death_count}", font=("Helvetica", 25))
        file.truncate()
        file.write(str(death_count))


root = tk.Tk()
count_button = tk.Button(root)
count_label = tk.Label(root)
count_display = tk.Message(root)
reset_button = tk.Button(root)

root.title("Death Counter")
root.geometry("290x240")
root.resizable(width=False, height=False)
root.config(bg="grey")

count_button.config(
    bg="#999999",
    fg="black",
    text="ADD",
    font=("Helvetica", 12, "bold"),
    command=increase_count,
)
count_label.config(
    bg="grey", fg="yellow", text="Deaths:", font=("Helvetica", 25, "bold")
)

count_display.config(
    text=death_count,
    font=("Helvetica, 25"),
    bg="grey",
    fg="yellow",
    relief=tk.SUNKEN,
)
reset_button.config(
    bg="#999999",
    fg="black",
    text="Reset",
    font=("Helvetica", 10, "bold"),
    command=reset_count,
)

count_button.place(relx=0.5, rely=0.65, anchor="center")
count_label.place(relx=0.5, rely=0.2, anchor="center")
count_display.place(relx=0.5, rely=0.45, anchor="center", width=100, height=40)
reset_button.place(relx=0.90, rely=0.94, anchor="center", width=50, height=20)

root.mainloop()
