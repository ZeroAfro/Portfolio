# Stylized GUI

# Imports
import tkinter
from tkinter import ttk
import sv_ttk

#modules
root = tkinter.Tk()
button = ttk.Button(root, text="Click me!")


# root window
root.title("Reading List")
root.geometry('900x600')










# Packs
button.pack()

# DO NOT MOVE
sv_ttk.set_theme("dark")

root.mainloop()