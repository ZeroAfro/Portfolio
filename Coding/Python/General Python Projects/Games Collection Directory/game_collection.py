import json
from pathlib import Path

# TODO: Add seperate file for just functions

main_menu = True
format_options = ["Physical", "Digital"]


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


def redundancy_check(game_title):
    """Checks if the entered title has already been entered"""

    if game_title in switch_titles:
        line_break()
        print(f"{game_title} already exists.")
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
    formated_game_count = f"You currently have a total of [{count}] games"
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

    prompt = f"{game_count()}\n"
    prompt += ("\nPlease enter the number for the option you wish to "
               "select:\n")
    prompt += "You can enter `q` at anytime to quit.\n"
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
                line_break()
                break
            elif redundancy_check(game_title):
                answer = input("\n\nWould you like to change the format for: "
                               f"{game_title}? (y/n): "
                               ).strip()
                if answer.lower() == "q":
                    line_break()
                    line_break()
                    break
                elif answer.lower() == "y":
                    print("Please enter one of the following options:\n"
                          "\n\t[1]: Both\n\t[2]: Physical\n\t[3]: Digital\n")

                    game_format = input("Game format: ").strip().title()

                    if game_format.lower() == "q":
                        line_break()
                        line_break()
                        break
                    elif game_format == "1":
                        new_format = "Physical/Digital"
                    elif game_format == "2":
                        new_format = "Physical"
                    elif game_format == "3":
                        new_format = "Digital"
                    else:
                        print("\nPlease enter a valid option of either "
                              "`1`, `2`, or '3'.\n")

                    add_title(game_title, new_format)
                    file_saving()
                    line_break()
                    break
                elif answer.lower() == "n":
                    line_break()
                    line_break()
                    break
                else:
                    print("\nPlease enter a valid option of either `y` or "
                          "`n`.\n")

            print(
                f"\n\nIn which format do you own {game_title}?\n\n"
                "Please enter one of the following options:\n"
                "\n\t[1]: Both\n\t[2]: Physical\n\t[3]: Digital\n"
                )

            game_format = input("Game Format: ").strip().title()

            if game_format.lower() == "q":
                line_break()
                line_break()
                break
            elif game_format == "1":
                game_format = "Physical/Digital"
                add_title(game_title, game_format)
                file_saving()
            elif game_format == "2":
                game_format = "Physical"
                add_title(game_title, game_format)
                file_saving()
            elif game_format == "3":
                game_format = "Digital"
                add_title(game_title, game_format)
                file_saving()
            else:
                print("\nPlease enter a valid option of either "
                      "`1`, `2`, or '3'.\n")

    elif prompt_answer == "2":
        while True:
            prompt = ("\nPlease enter the number for the type of game format "
                      "you wish to view:\n")
            prompt += "\n\t[1]: All\n\t[2]: Physical\n\t[3]: Digital\n"
            print(prompt)

            answer = input("Option: ").strip()

            if answer.lower() == "q":
                line_break()
                line_break()
                break
            elif answer.lower() == "1":
                switch_titles = file_loading(path)

                if len(switch_titles) > 0:
                    line_break()
                    for title in switch_titles.keys():
                        print(f"{title}")
                    line_break()
                    print(game_count())
                    line_break()
                else:
                    line_break()
                    print("\n[Your collection is currently empty.]\n")

            elif answer.lower() == "2":
                switch_titles = file_loading(path)

                if len(switch_titles) > 0:
                    search_terms = ("Physical", "Physical/Digital")
                    temp_list = []
                    line_break()

                    for title, tags in switch_titles.items():
                        for format in tags.values():
                            if format in search_terms:
                                print(f"{title}")
                                temp_list.append(title)
                    line_break()
                    print(f"You have [{len(temp_list)}] Physical games.")
                    line_break()
                else:
                    line_break()
                    print("\n[Your collection is currently empty.]\n")

            elif answer.lower() == "3":
                switch_titles = file_loading(path)

                if len(switch_titles) > 0:
                    search_terms = ("Digital", "Physical/Digital")
                    temp_list = []
                    line_break()

                    for title, tags in switch_titles.items():
                        for format in tags.values():
                            if format in search_terms:
                                print(f"{title}")
                                temp_list.append(title)
                    line_break()
                    print(f"You have [{len(temp_list)}] Digital games.")
                    line_break()
                else:
                    line_break()
                    print("\n[Your collection is currently empty.]\n")

            else:
                print("\nPlease enter a valid option of either "
                      "`1`, `2`, or '3'.\n")
    else:
        print("\nPlease enter a valid option of either `1` or `2`.\n")
