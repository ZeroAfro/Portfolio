# Reading Tracker W/GUI

import tkinter as tk
import os
import random
from tkinter import messagebox

# Function that grabs and filters titles entered
def get_title():
    
    title = title_entry_box.get().strip().title()
    title = title.replace("â€™S", "'s")
    title = title.replace("â€™R", "'r")
    title = title.replace("'S", "'s")
    title = title.replace("I'M", "I'm")
    title = title.replace("'T", "'t")
    title = title.replace("'Re", "'re")
    
    if title == "":
        messagebox.showerror("ERROR", "No title was entered!", parent=root)
        return
    
    try:
        with open('Reading List.txt', 'r+') as file:
            lines = file.readlines()
        if any(title in line for line in lines):
            title_entry_box.delete(0, tk.END)
            messagebox.showerror("ERROR", "List already contains this title!", parent=root)
        else:
            file_write(title)
            
    except FileNotFoundError:
            file_write(title)
            
 # Function that returns a random title
def random_title():  
    try:
        
        file_size = os.path.getsize('Reading List.txt')

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
        
# Writes title into txt and erases entry box
def file_write(title):
    with open('Reading List.txt', 'a') as file:
                file.write(f"[{title}]\n")
                title_entry_box.delete(0, tk.END)
    
# launches file sit to variable
def launch_file():
    os.startfile('Reading List.txt')
    
# Allows ESC to close GUI
def esc_bind():
    root.destroy()
    
# Customization variables
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

# Root window config
root.title("Reading Tracker")
root.geometry("900x600")
root.resizable(width=False, height=False)
root.config(
    bg="light blue",
    highlightcolor="#0372FE",
    highlightthickness=1.5
)

title_entry_label.config(
    text="Title",
    fg=label_fg,
    bg=label_bg,
    font=("segoe", 25, "bold")
)

random_title_label.config(
    text="Random Title",
    fg=label_fg,
    bg=label_bg,
    font=("segoe", 25, "bold")
)

random_title_button.config(
    text="RANDOM",
    width=10,
    height=2,
    bg=button_bg,
    fg=button_fg,
    command=random_title
)

text_file_button.config(
    text="OPEN",
    width=10,
    height=2,
    bg=button_bg,
    fg=button_fg,
    command=launch_file
)

title_entry_box.config(
    fg=box_fg,
    bg=box_bg,
    font=("segoe", 10, "bold")
)

random_title_box.config(
    fg=box_fg,
    bg=box_bg,
    relief=tk.SUNKEN
)

title_entry_box.place(relx=0.5, rely=0.42, anchor="center", width=600, height=25)
random_title_box.place(relx=0.5, rely=0.70, anchor="center", width=600, height=25)

random_title_button.place(relx=0.5, rely=0.80, anchor="center")
text_file_button.place(relx=0.89, rely=0.03)

title_entry_label.place(relx=0.5, rely=0.35, anchor="center", width=500, height=25)
random_title_label.place(relx=0.5, rely=0.63, anchor="center", width=500, height=25)

# Keybinds
title_entry_box.bind("<Return>", lambda event: get_title())
root.bind("<Escape>", lambda event: esc_bind())

# event loop
root.mainloop()
