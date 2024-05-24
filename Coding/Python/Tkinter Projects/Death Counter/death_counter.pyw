import tkinter as tk


# variables
death_count = 0

# Displays a incramental death count
def count():
    global death_count
    death_count += 1
    count_display.config(text=f"{death_count}", font=('Helvetica', 25))
    

# widgets
root=tk.Tk()
count_button=tk.Button(root)
count_label=tk.Label(root)
count_display=tk.Message(root)


# root options
root.title("Death Counter")
root.geometry('290x240')
root.resizable(width=False, height=False)

root.config(
    bg='grey'
)

count_button.config(
    bg='#999999',
    fg='black',
    text="Click",
    font=('Helvetica', 12, 'bold'),
    command=count
)
count_label.config(
    bg='grey',
    fg='yellow',
    text="Deaths:",
    font=('Helvetica', 25, 'bold')
)

count_display.config(
    bg='grey',
    fg='yellow',
    relief=tk.SUNKEN
)


count_button.place(relx=0.5, rely=0.7, anchor='center')
count_label.place(relx=0.5, rely=.2, anchor='center')
count_display.place(relx=0.5, rely=0.45, anchor='center', width=100, height=40)


# event loop
root.mainloop()