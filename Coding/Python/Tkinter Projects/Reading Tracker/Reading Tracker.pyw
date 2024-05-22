# GUI for reading list

# TODO: Finalize positions of widgets

# Library Imports
import tkinter as tk
import os
import random
from tkinter import messagebox

# Setting up the absolute path for the file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(os.getcwd(), 'Reading List.txt')

# grabs text from entry box and writes it into file
def get_title():
    
    title = title_entry_box.get().strip().title()
    
    if title == "":
        messagebox.showerror("ERROR", "No title was entered!", parent=root)
        return
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        if any(title in line for line in lines):
            title_entry_box.delete(0, tk.END)
            messagebox.showerror("ERROR", "List already contains this title!", parent=root)
        else:
            title = title.replace("â€™S", "'s")
            title = title.replace("'S", "'s")
            file_write(title)
            
    except FileNotFoundError:
            title = title.replace("â€™S", "'")
            title = title.replace("'S", "'s")
            file_write(title)
            
 # grabs a random title from the file and returns it
def random_title():  
    try:
        
        file_size = os.path.getsize(file_path)

        if(file_size == 0):
            messagebox.showerror("ERROR", "List is empty", parent=root)
        else:
            with open('Reading List.txt', 'r') as file:
                lines = file.readlines()
                choice = random.choice(lines).strip()
                width = len(choice) * 10
                font = font=("tahoma", 10, "bold")
                random_title_box.config(text=choice, width=width, font=font)
    except FileNotFoundError:
        messagebox.showerror("ERROR", "List file does not exist", parent=root)
        
# adding title into file
def file_write(title):
    with open(file_path, 'a') as file:
                file.write(f"[{title}]\n")
                title_entry_box.delete(0, tk.END)
    
# launches file sit to variable
def launch_file():
    os.startfile(file_path)
    
# binds escape to closing tkinter window
def esc_bind():
    root.destroy()
    
# Variables
#spell = Speller(fast=True)
button_bg = "#F4F3ED"
button_fg = "black"
label_fg = "black"
label_bg = "light blue"
box_bg = "#ECE9D8"
box_fg = "black"

# Widgets
root = tk.Tk()
title_entry_label = tk.Label()
title_entry_box = tk.Entry()
random_title_button = tk.Button()
random_title_box = tk.Message(root)
random_title_label = tk.Label()
text_file_button = tk.Button()

# Center frame
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = screen_height // 2
center_y = screen_height // 2
center_frame = tk.Frame(root)

# Root window
root.title("Reading Tracker")
root.geometry("900x600")
root.resizable(width=False, height=False)
root.config(
    bg="light blue",
    highlightcolor="#0372FE",
    highlightthickness=1.5
)

# Label for title entry box
title_entry_label.config(
    text="Title",
    fg=label_fg,
    bg=label_bg,
    font=("segoe", 25, "bold")
)

# Label for random title box
random_title_label.config(
    text="Random Title",
    fg=label_fg,
    bg=label_bg,
    font=("segoe", 25, "bold")
)

# Random button
random_title_button.config(
    text="RANDOM",
    width=10,
    height=2,
    bg=button_bg,
    fg=button_fg,
    command=random_title
)

# Text file button
text_file_button.config(
    text="OPEN",
    width=10,
    height=2,
    bg=button_bg,
    fg=button_fg,
    command=launch_file
)

# Title input window
title_entry_box.config(
    fg=box_fg,
    bg=box_bg,
    font=("segoe", 10, "bold")
)

# Random output window
random_title_box.config(
    fg=box_fg,
    bg=box_bg,
    relief=tk.SUNKEN
)

# boxes
title_entry_box.place(relx=0.5, rely=0.42, anchor="center", width=600, height=25)
random_title_box.place(relx=0.5, rely=0.70, anchor="center", width=600, height=25)

# buttons
random_title_button.place(relx=0.5, rely=0.80, anchor="center")
text_file_button.place(relx=0.89, rely=0.03)

# labels
title_entry_label.place(relx=0.5, rely=0.35, anchor="center", width=500, height=25)
random_title_label.place(relx=0.5, rely=0.63, anchor="center", width=500, height=25)

# Keybinds
title_entry_box.bind("<Return>", lambda event: get_title())
root.bind("<Escape>", lambda event: esc_bind())

# event loop
root.mainloop()