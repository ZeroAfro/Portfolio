"""
Reading tracker to track novels/books/manwah I wish to read
and allows me to pull a random title
"""

import tkinter as tk
import os
import random
from tkinter import messagebox


def get_title():
    """Grabs title and filters for common issues"""

    # When copy/pasting titles from aggregator sites
    # these are common formating issues that will come up
    title = title_entry_box.get().strip().title()
    title = title.replace("â€™S", "'s")
    title = title.replace("â€™R", "'r")
    title = title.replace("'S", "'s")
    title = title.replace("I'M", "I'm")
    title = title.replace("'T", "'t")
    title = title.replace("'Re", "'re")

    if title == "":
        messagebox.showerror("ERROR", "No title was entered!", parent=root)
    try:
        with open("Reading List.txt", "r+") as file:
            lines = file.readlines()

        # Searches line for line to see if any of the currently saved titles
        # matches the currently entered title and that the
        # title you entered wasn't blank
        if any(title in line for line in lines) and title != "":
            title_entry_box.delete(0, tk.END)
            messagebox.showerror(
                "ERROR", "List already contains this title!", parent=root
            )
        else:
            file_write(title)
    except FileNotFoundError:
        file_write(title)


def random_title():
    """Grabs and displays random title"""

    try:

        file_size = os.path.getsize("Reading List.txt")

        if file_size == 0:
            messagebox.showerror("ERROR", "List is empty", parent=root)
        else:
            with open("Reading List.txt", "r") as file:
                lines = file.readlines()
                choice = random.choice(lines).strip()
                width = len(choice) * 10
                font = font = ("tahoma", 10, "bold")
                random_title_box.config(text=choice, width=width, font=font)
    except FileNotFoundError:
        messagebox.showerror("ERROR", "List file does not exist", parent=root)


def file_write(title):
    """Erases title from entry box and writes it to txt file"""

    with open("Reading List.txt", "a") as file:
        file.write(f"{title}\n")
        title_entry_box.delete(0, tk.END)


def launch_file():
    """Opens file when button is pressed"""

    os.startfile("Reading List.txt")


def esc_bind():
    """Binds the 'ESC' key to closing the window"""

    root.destroy()


button_bg = "#ff4d4d"
button_fg = "black"
label_fg = "#ff4d4d"
label_bg = "#1c1c1c"
box_bg = "#1c1c1c"
box_fg = "#ff4d4d"

root = tk.Tk()
title_entry_label = tk.Label()
title_entry_box = tk.Entry()
random_title_button = tk.Button()
random_title_box = tk.Message(root)
random_title_label = tk.Label()
text_file_button = tk.Button()

root.title("Reading Tracker")
root.iconbitmap("resources/book.ico")
root.geometry("900x600+490+200")
root.resizable(width=False, height=False)
root.config(bg="#1c1c1c", highlightcolor="#2e2e2e", highlightthickness=1.5)
title_entry_label.config(
    text="Title",
    fg=label_fg,
    bg=label_bg,
    font=("segoe", 25, "bold"),
)
random_title_label.config(
    text="Random Title", fg=label_fg, bg=label_bg, font=("segoe", 25, "bold")
)
random_title_button.config(
    text="RANDOM",
    width=10,
    height=2,
    bg=button_bg,
    fg=button_fg,
    command=random_title,
)
text_file_button.config(
    text="OPEN",
    width=10,
    height=2,
    bg=button_bg,
    fg=button_fg,
    command=launch_file,
)

title_entry_box.config(
    fg=box_fg,
    bg=box_bg,
    font=("segoe", 10, "bold"),
    insertbackground="#ff4d4d",
)
random_title_box.config(fg=box_fg, bg=box_bg, relief=tk.SUNKEN)

title_entry_box.place(
    relx=0.5,
    rely=0.42,
    anchor="center",
    width=600,
    height=25,
)
random_title_box.place(
    relx=0.5,
    rely=0.70,
    anchor="center",
    width=600,
    height=25,
)

random_title_button.place(relx=0.5, rely=0.80, anchor="center")
text_file_button.place(relx=0.89, rely=0.03)

title_entry_label.place(
    relx=0.5,
    rely=0.35,
    anchor="center",
    width=500,
    height=25,
)
random_title_label.place(
    relx=0.5,
    rely=0.63,
    anchor="center",
    width=500,
    height=25,
)

title_entry_box.bind("<Return>", lambda event: get_title())
root.bind("<Escape>", lambda event: esc_bind())

root.mainloop()
