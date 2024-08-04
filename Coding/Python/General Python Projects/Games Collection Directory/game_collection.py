import json
from pathlib import Path

# TODO: Add error checking
# TODO: Format code better

main_menu = True


def main():
    """Main Function"""

    path = Path("game_collection.json")

    if path.exists():
        if path.stat().st_size > 0:
            try:
                switch_titles = json.loads(path.read_text())
            except (json.JSONDecodeError, IOError):
                print(f"\nDetected an error with [\033[1m{path}\033[0m], "
                      "please check for invalid formating and "
                      "user/file permissions\n")
                quit()
        else:
            new_list(path)
            switch_titles = file_loading()

    else:
        new_list(path)
        switch_titles = file_loading()

    return switch_titles, path


def redundancy_check(game):
    """Checks if the entered title has already been entered"""

    if game in switch_titles:
        line_break()
        print(f"{game} already exists, please check and try again.")
        return True
    return False


def file_saving():
    """Saves current titles to JSON file"""

    try:
        path.write_text(json.dumps(switch_titles, indent=4, ensure_ascii=False,
                                   sort_keys=True))
    except PermissionError:
        print(f"\nCannot save data to [\033[1m{path}\033[0m] due to a "
              "permissions error. Please check your user/file permissions "
              "and try again.\n")


def file_loading():
    """Loads currently saved game titles from JSON file"""

    switch_titles = json.loads(path.read_text())

    return switch_titles


def new_list(path):
    """Overrides the file with a blank dictionary"""

    switch_titles = {}
    path.write_text(json.dumps(switch_titles))


def add_title(game_title, game_format):
    """Adds title into dictionary"""

    switch_titles[game_title] = {
        "Format": game_format
        }


def game_count():
    """Returns the number of games in the collection"""

    count = len(switch_titles)
    formated_game_count = f"You currently have \033[1m{count}\033[0m games"
    formated_game_count += " in your collection!"

    return formated_game_count


def quitting():
    """Saves the currently saved titles and quits"""

    file_saving()
    quit()


def line_break():
    """Adds a line break"""

    print("\n")


if __name__ == "__main__":
    switch_titles, path = main()

while main_menu:
    prompt = "\nWelcome to your Game Collection!\n\n"
    prompt += f"{game_count()}"
    prompt += ("\n\nPlease enter the number for the option you wish to "
               "select:\n")
    prompt += "You can enter `q` at anytime to quit.\n"
    prompt += ("\n[1]: Add titles to collecton\n[2]: View game "
               "collection\n")
    print(prompt)

    prompt_answer = input("Option: ").strip()

    if prompt_answer == "1":

        while True:
            game_title = input("\nGame Title: ")

            if redundancy_check(game_title):
                answer = input("\nWould you like to add "
                               f"another format for {game_title}? (y/n):"
                               ).strip()

                if answer.lower() == "y":
                    print
                    game_format = input("Game format: ").title()

                    existing_game_format = (
                        switch_titles[game_title].get("Format", "")
                        )

                    new_format = (
                        f"{existing_game_format}/{game_format}"
                        )

                    add_title(game_title, new_format)
                    line_break()
                    break

                elif answer.lower() == "n":
                    break

                elif answer.lower() == "q":
                    break

                else:
                    print("\nPlease enter a valid option of either `y` or "
                          "`n`.\n")

            elif game_title.lower() == "q":
                break

            game_format = input("Game Format: ").title()

            if game_format.lower() == "q":
                break

            add_title(game_title, game_format)
            print(f"\n{game_count()}\n")

    elif prompt_answer == "2":
        while True:
            prompt = ("\nPlease enter the number for the type of game format "
                      "you wish to view:\n")
            prompt += "\n[1]: All\n[2]: Physical\n[3]: Digital\n"
            print(prompt)

            answer = input("Option: ").strip()

            if answer == "1":
                switch_titles = file_loading()
                if len(switch_titles) > 0:
                    line_break()
                    for title in switch_titles.keys():
                        print(f"{title}")
                    line_break()
                else:
                    print(f"\nThere are [\033[1m{len(switch_titles)}\033[0m] "
                          "games in your collection.\n")
                    break

            elif answer.lower() == "2":
                switch_titles = file_loading()
                if len(switch_titles) > 0:
                    search_terms = ["Physical", "Physical/Digital",
                                    "Digital/Physical"]
                    line_break()
                    for title, tags in switch_titles.items():
                        for format in tags.values():
                            if format in search_terms:
                                print(f"{title}")
                    line_break()
                else:
                    print(f"\nThere are [\033[1m{len(switch_titles)}\033[0m] "
                          "games in your collection.\n")
                    break

            elif answer.lower() == "3":
                switch_titles = file_loading()
                if len(switch_titles) > 0:
                    search_terms = ["Digital", "Digital/Physical",
                                    "Physical/Digital"]
                    line_break()
                    for title, tags in switch_titles.items():
                        for format in tags.values():
                            if format in search_terms:
                                print(f"{title}")
                else:
                    print(f"\nThere are [\033[1m{len(switch_titles)}\033[0m] "
                          "games in your collection.\n")
                break

            elif answer.lower() == "q":
                break

            else:
                print("\nPlease enter a valid option of either "
                      "`1`, `2`, or '3'.\n")

    elif prompt_answer.lower() == "q":
        quitting()
    else:
        print("\nPlease enter a valid option of either `1` or `2`.\n")
