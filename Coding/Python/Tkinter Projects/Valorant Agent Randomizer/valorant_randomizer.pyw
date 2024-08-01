"""
A randomizer for the game 'Valorant'.
It pulls a random value out of the list and displays it
"""

import tkinter as tk
from PIL import Image, ImageTk
import random

"""Currently has all released agents as of patch 8.05"""

agents = [
    "brimstone",
    "clove",
    "harbor",
    "omen",
    "viper",
    "chamber",
    "cypher",
    "deadlock",
    "killjoy",
    "sage",
    "fade",
    "gekko",
    "KAY/0",
    "sova",
    "iso",
    "jett",
    "neon",
    "phoenix",
    "raze",
    "reyna",
    "yoru",
    "astra",
    "skye",
    "breach",
]


previous_agent = None


def randomize():
    """Randomizes agent"""

    global previous_agent

    random_agent_box.place(
        x=300,
        y=320,
        anchor="n",
    )

    while True:
        # Checks if the previous agent is the same as the currently
        # selected agent and if it is then it generates another
        # agent and also filters out 'KAY/0' from being formated
        random_agent = random.choice(agents)

        if random_agent != previous_agent and random_agent != "KAY/0":
            random_agent_title = random_agent.title()
            random_agent_box.config(text=f"►{random_agent_title}◄")
            previous_agent = random_agent
            break

        elif random_agent != previous_agent and random_agent == "KAY/0":
            random_agent_box.config(text=f"►{random_agent}◄")
            previous_agent = random_agent
            break


def esc_bind():
    "Binds 'ESC' key to closing window"

    root.destroy()


root = tk.Tk()
root.title("Valorant Randomizer")
root.iconbitmap("resources/val_icon.ico")
root.config(background="white")
root.geometry("600x500+700+250")
root.resizable(width=False, height=False)

bg_image = Image.open("resources/val_logo.png")
bg_image = bg_image.resize((600, 500))

root_bg = ImageTk.PhotoImage(bg_image)

background_image = tk.Label(root, image=root_bg)
background_image.pack(fill=tk.BOTH, expand=True)

random_button = tk.Button(root)
random_agent_box = tk.Label(root)

random_agent_box.config(
    bg="white",
    fg="#ff4654",
    relief="sunken",
    font=(
        "Helvectica",
        15,
    ),
    justify="center",
)

random_agent_box.place_forget()

root.bind("<Return>", lambda event: randomize())
root.bind("<Escape>", lambda event: esc_bind())

root.mainloop()
