import json
from pathlib import Path

main_menu = True


def main():
    """Main Function"""

    path = Path("game_collection.json")

    if path.exists():
        if path.stat().st_size > 0:
            try:
                switch_titles = json.loads(path.read_text())
            except (json.JSONDecodeError, IOError):
                print(f"\nDetected an error with [{path}].\n"
                      "Please check for invalid formating and "
                      "user/file permissions\n")
                input("Press 'ENTER' to exit")
                quit()
        else:
            new_list(path)
            switch_titles = file_loading(path)
    else:
        new_list(path)
        switch_titles = file_loading(path)

    return switch_titles, path


def redundancy_check(game):
    """Checks if the entered title has already been entered"""

    if game in switch_titles:
        line_break()
        print(f"{game} already exists.")
        return True
    return False


def file_saving():
    """Saves current titles to JSON file"""

    try:
        path.write_text(json.dumps(switch_titles, indent=4, ensure_ascii=False,
                                   sort_keys=True))
    except (PermissionError, FileNotFoundError)as error:
        if isinstance(error, PermissionError):
            print(f"\nCannot save data to [{path}] due to a "
                  "permissions error.\nPlease check your user/file "
                  "permissions and try again.\n")
            error_stall()
        elif isinstance(error, FileNotFoundError):
            print(f"\n[{path}] was created since it could not "
                  "be found.\n")
        else:
            print("\nAn unexpected error has occured.\n")
            error_stall()


def file_loading(path):
    """Loads currently saved game titles from JSON file"""

    switch_titles = json.loads(path.read_text())

    return switch_titles


def new_list(path):
    """Overrides the file with a blank dictionary"""

    switch_titles = {}
    try:
        path.write_text(json.dumps(switch_titles))
    except PermissionError:
        print(f"\nCannot save data to [{path}] due to a "
              "permissions error.\nPlease check your user/file permissions "
              "and try again.\n")
        error_stall()


def add_title(game_title, game_format):
    """Adds title into dictionary"""

    switch_titles[game_title] = {
        "Format": game_format
        }


def game_count():
    """Returns the number of games in the collection"""

    count = len(switch_titles)
    formated_game_count = f"You currently have [{count}] games"
    formated_game_count += " in your collection!"

    return formated_game_count


def quitting():
    """Saves the currently saved titles and quits"""

    file_saving()
    quit()


def error_stall():
    """
    Wait for user input to allow the error message to be read then it quits
    """

    input("Press 'ENTER' to exit")
    quit()


def line_break():
    """Adds a line break"""

    print("\n")


if __name__ == "__main__":
    switch_titles, path = main()

print("\nWelcome to your Game Collection!\n")

while main_menu:

    prompt = ("\nPlease enter the number for the option you wish to "
              "select:\n")
    prompt += "You can enter `q` at anytime to quit.\n\n"
    prompt += f"{game_count()}"
    prompt += ("\n\n\t[1]: Add titles to collecton\n\t[2]: View game "
               "collection\n")
    print(prompt)

    prompt_answer = input("Option: ").strip()

    if prompt_answer.lower() == "q":
        quitting()

    elif prompt_answer == "1":
        while True:
            game_title = input("\nGame Title: ").strip()

            if game_title.lower() == "q":
                line_break()
                break
            elif redundancy_check(game_title):
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
                    file_saving()
                    line_break()
                    break
                elif answer.lower() == "n":
                    break
                elif answer.lower() == "q":
                    break
                else:
                    print("\nPlease enter a valid option of either `y` or "
                          "`n`.\n")

            game_format = input("Game Format: ").strip().title()

            if game_format.lower() == "q":
                line_break()
                break
            elif game_title and game_format:
                add_title(game_title, game_format)
                file_saving()

    elif prompt_answer == "2":
        while True:
            prompt = ("\nPlease enter the number for the type of game format "
                      "you wish to view:\n")
            prompt += "\n\t[1]: All\n\t[2]: Physical\n\t[3]: Digital\n"
            print(prompt)

            answer = input("Option: ").strip()

            if answer.lower() == "1":
                switch_titles = file_loading(path)
                if len(switch_titles) > 0:
                    line_break()
                    for title in switch_titles.keys():
                        print(f"{title}")
                    line_break()
                else:
                    line_break()
                    print("\n[Your collection is currently empty.]\n")

            elif answer.lower() == "2":
                switch_titles = file_loading(path)
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
                    line_break()
                    print("\n[Your collection is currently empty.]\n")

            elif answer.lower() == "3":
                switch_titles = file_loading(path)
                if len(switch_titles) > 0:
                    search_terms = ["Digital", "Digital/Physical",
                                    "Physical/Digital"]
                    line_break()
                    for title, tags in switch_titles.items():
                        for format in tags.values():
                            if format in search_terms:
                                print(f"{title}")
                    line_break()
                else:
                    line_break()
                    print("\n[Your collection is currently empty.]\n")

            elif answer.lower() == "q":
                break

            else:
                print("\nPlease enter a valid option of either "
                      "`1`, `2`, or '3'.\n")
    else:
        print("\nPlease enter a valid option of either `1` or `2`.\n")
