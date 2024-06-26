# Stylized GUI

import tkinter
from tkinter import ttk
import sv_ttk

root = tkinter.Tk()
button = ttk.Button(root, text="Click me!")

root.title("Reading List")
root.geometry('900x600')

button.pack()

# DO NOT MOVE
sv_ttk.set_theme("dark")

root.mainloop()