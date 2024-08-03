"""Tracks and Sorts Switch Games to a JSON file as a formated list"""

from pathlib import Path
import json


def main():
    """Main function, sets path and checks for errors and if path exists"""

    path = Path("switch_game_list.json")

    if path.exists():

        if path.stat().st_size > 0:
            try:
                contents = path.read_text()
                titles = json.loads(contents)
            except (json.JSONDecodeError, IOError):

                titles = main_error_handling(path)

        else:
            add_line_break()
            print(f"The file [{path}] is currently empty. Initializing with "
                  "an empty list.")
            add_line_break()
            titles = []
            path.write_text(json.dumps(titles))

    else:
        titles = []
        path.write_text(json.dumps(titles))

    return titles, path


def main_error_handling(path):
    """Handles the majority of the error checking for main function"""

    add_line_break()
    print(f"Detected a problem with trying to read the file: [{path}].")
    add_line_break()

    prompt = input("Would you like to try to override and rewrite the "
                   "file? (y/n): ").strip()

    if prompt == "y".lower():
        titles = []
        path.write_text(json.dumps(titles))
        add_line_break()
        print(f"File [{path}] has been rewritten.")
        add_line_break()

    elif prompt == "n".lower():
        add_line_break()
        print(f"Please check the file {path} for any errors such as invalid "
              "JSON strings.")
        add_line_break()
        input("Press 'ENTER' to exit.")

        quit()

    else:
        add_line_break()
        print("Please enter a valid option of either 'y' or 'n'.")
        add_line_break()

    return titles


def add_line_break():
    """Adds spacing for better formatting"""

    print("\n")


if __name__ == "__main__":
    titles, path = main()

    print(
        "\nWelcome to the Switch Games List.\n\n"
        "At any time type 'q' to quit or 'v' to view your sorted "
        "list of games.\n\n"
        "Please note that the any added titles will not save unless you type "
        "'q' to exit.\n"
          )

    while True:
        switch_title = input("Switch Title: ").strip()

        if switch_title.lower() == "q":
            titles.sort()
            try:
                #  Indents the list for better readability and deals with
                #  special ascii characters
                path.write_text(json.dumps(titles, ensure_ascii=False,
                                           indent=4))
                break
            except PermissionError:
                add_line_break()
                print("You do not have permission to save to the file: "
                      f"[{path}]"
                      "\nPlease check your user/folder permissions.")
                add_line_break()
                input("Press 'ENTER' to exit.")
                break

        elif switch_title.lower() == "v":
            sorted_titles = sorted(titles, key=str.lower)
            add_line_break()
            for title in sorted_titles:
                print(f"\t{title}")
            add_line_break()

        elif switch_title.isdigit():
            add_line_break()
            print("Please enter a valid title.")
            add_line_break()

        else:
            try:
                saved_titles = json.loads(path.read_text())
            except PermissionError:
                add_line_break()
                print(f"You do not have permission to load the file [{path}]\n"
                      "Please check your user/folder permissions.")
                add_line_break()
                input("Press 'ENTER' to exit.")
                break

            if switch_title in titles or switch_title in saved_titles:
                add_line_break()
                print("That title is already in your list, "
                      "please check it and try again.")
                add_line_break()

            else:
                titles.append(switch_title)
