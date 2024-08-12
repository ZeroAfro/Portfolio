"""Script to catalog how many of the different rarities I own"""

import json
from pathlib import Path

# TODO: Add error handling for jsondecone/io/permissions


class Card:
    """Models a TCG card"""

    VALID_RARITIES: tuple = ("R", "SR", "CR", "SCR", "PTR", "SER")

    def __init__(self) -> None:
        self.cards: dict = {
            "R": 0,
            "SR": 0,
            "CR": 0,
            "SCR": 0,
            "PTR": 0,
            "SER": 0
            }

    def set_rarity(self) -> None:
        """Records card rarity to dictionary"""

        self.cards[card_rarity.upper()] += 1
        self.saving_dictionary(path)

    def print_dictionary(self) -> dict[str, int]:
        """Returns a formated box of the curreny dictionary key: value pairs"""

        formated_rarities = "+---------------------+\n"
        formated_rarities += "|    Rarity Count     |\n"
        formated_rarities += "+---------------------+\n"
        formated_rarities += f"|   Total Cards: {self.card_total():<5}|\n"
        formated_rarities += "|                     |\n"

        for rarity, count in self.cards.items():

            if len(rarity) == 1:
                formated_rarities += f"| {rarity}: {count:<17}|\n"
            elif len(rarity) == 2:
                formated_rarities += f"| {rarity}: {count:<16}|\n"
            elif len(rarity) == 3:
                formated_rarities += f"| {rarity}: {count:<15}|\n"
            else:
                formated_rarities += f"| {rarity}: {count:<18}|\n"

        formated_rarities += "+---------------------+\n"
        return formated_rarities

    def update_count(self, rarity: str, new_value: int) -> None:
        """Changes the values of any of the dictionary key: value pairs"""

        self.cards[rarity] = new_value
        self.saving_dictionary(path)

    def saving_dictionary(self, path) -> None:
        """Saves the dictionary to JSON file."""

        path.write_text(json.dumps(self.cards, indent=4))


def main() -> tuple[Path, dict[str, int]]:
    """Main Function"""

    path = Path("tcg_collection.json")

    if path.exists() and path.stat().st_size > 0:
        cards = json.loads(path.read_text())
    else:
        place_holder_dict: dict = {
            "R": 0,
            "SR": 0,
            "CR": 0,
            "SCR": 0,
            "PTR": 0,
            "SER": 0
            }
        path.write_text(json.dumps(place_holder_dict, indent=4))
        cards = place_holder_dict

    return path, cards


def line_break() -> None:
    """Adds a line break"""

    print("\n")


if __name__ == "__main__":
    path, cards = main()
    new_card = Card()
    new_card.cards = cards


while True:
    prompt = ("Would you like to input, view, or change your current "
              "rarities?:")
    prompt += ("\nEnter 'q' at anytime to quit.\n\n")
    prompt += ("\t[1]: Input\n\t[2]: View\n\t[3]: Change\n")
    print(prompt)

    prompt_response = input("Response: ")

    if prompt_response.lower() == "q":
        path.write_text(json.dumps(new_card.cards, indent=4))
        raise SystemExit
    elif prompt_response == "1":

        while True:
            print("\n\nPlease enter one of the following:\n"
                  f"\n\t{str(new_card.VALID_RARITIES)}\n"
                  .replace(",", " |")
                  .replace("'", "")
                  .replace("(", "")
                  .replace(")", "")
                  )
            card_rarity = input("Rarity: ")
            if card_rarity == "q":
                break
            elif card_rarity.upper() in new_card.VALID_RARITIES:

                new_card.set_rarity()

                print(f"\n\n\t---'{card_rarity.upper()}' rarity "
                      "card has been added!---")
            else:
                print(f"\n\n{card_rarity} is not a valid response.\n\n")
                input("Press 'ENTER' to continue")

    elif prompt_response == "2":
        print(f"\n\n{new_card.print_dictionary()}")
        input("Press 'ENTER' to continue")
        line_break()
        line_break()
    elif prompt_response == "3":

        while True:
            print("\n\nPlease enter one of the following rarities:\n"
                  f"\n\t{str(new_card.cards)}\n"
                  .replace(",", " |")
                  .replace("'", "")
                  .replace("{", "")
                  .replace("}", "")
                  )

            rarity = input("Rarity: ")

            if rarity.lower() == "q":
                line_break()
                line_break()
                break
            elif rarity.upper() in new_card.VALID_RARITIES:

                rarity = rarity.upper()

                print("\n\n\t---You currently have "
                      f"[{new_card.cards[rarity]}] "
                      f"'{rarity}' rarity cards.---\n")

                while True:
                    new_value = input("\nWhat would you like the new count "
                                      "to be?: ")
                    if new_value == "q":
                        line_break()
                        line_break()
                        break
                    elif new_value.isdigit():

                        new_value = int(new_value)

                        new_card.update_count(rarity, new_value)

                        print(f"\n\n\t---Your '{rarity}' rarity card count "
                              f"has been updated to {new_card.cards[rarity]}"
                              "---\n")
                        break
                    else:
                        print("\n\nPlease enter a valid whole number.\n\n")
                        input("Press 'ENTER' to continue")

            else:
                print("\n\nPlease enter a valid rarity tag.\n\n")
                input("Press 'ENTER' to continue\n\n")

    else:
        print("\n\nPlease enter a valid option of either '1' or '2'.\n\n")
        input("Press 'ENTER' to continue\n\n")

