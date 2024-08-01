"""Tracks and sorts switch games"""

from pathlib import Path
import json


def main():
    path = Path("switch_game_list.json")
    if path.exists():
        try:
            contents = path.read_text()
            titles = json.loads(contents)
        except (json.JSONDecodeError, IOError):
            titles = []
    else:
        titles = []
    return titles, path


def add_line_break():
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
            path.write_text(json.dumps(titles, ensure_ascii=False, indent=4))
            break

        elif switch_title.lower() == "v":
            try:
                saved_titles = json.loads(path.read_text())
                add_line_break()
                for title in saved_titles:
                    print(f"\t{title}")
                add_line_break()
            except (json.JSONDecodeError, IOError):
                print("Error reading the list.")
                add_line_break()

        elif switch_title.isdigit():
            add_line_break()
            print("Please enter a valid title.")
            add_line_break()

        else:
            titles.append(switch_title)
