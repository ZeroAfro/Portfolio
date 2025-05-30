"""
FFXIV Character Creation Randomizer

This lets you randomize the creation of a character from the
MMORPG 'FFXIV'.

You can randomize the whole creation or just specific parts of the creation.
"""

import random

main = True
sub_main = True
race_clan_selection = True
gender_selection = False
class_specialization_selection = False
deity_selection = False
character_description = False


def error_prompt():
    """Promps the user to enter a valid option if a invalid is entered."""

    print("\nPlease enter a valid option.\n")


def race_clan_deactivation():
    """
    Deactivates the section for choosing race/clan
    and activates the secion for selecting the gender.
    """

    global gender_selection
    global race_clan_selection

    gender_selection = True
    race_clan_selection = False


def gender_selection_deactivation():
    """
    Deactivates the section for choosing gender
    and activates the secion for selecting the class.
    """

    global class_specialization_selection
    global gender_selection

    class_specialization_selection = True
    gender_selection = False


def class_specialization_deactivation():
    """
    Deactivates the section for choosing class/class
    specialization and activates the secion for selecting
    the deity.
    """

    global deity_selection
    global class_specialization_selection

    deity_selection = True
    class_specialization_selection = False


def deity_selection_deactivation():
    """
    Deactivates the section for choosing deity
    and activates the secion that displays your character.
    """

    global character_description
    global deity_selection

    character_description = True
    deity_selection = False


class Character:
    """
    Models a character from the MMORPG 'FFXIV'
    with the various options you can choose during
    character creation.
    """

    def __init__(
        self,
        race=None,
        clan=None,
        gender=None,
        starting_class=None,
        deity=None,
        specialization=None,
    ):
        self.race = race
        self.clan = clan
        self.gender = gender
        self.starting_class = starting_class
        self.deity = deity
        self.specialization = specialization

    def random_race(self):
        """
        Randomizes the characters race and/or clan based
        on current attribute values.

        - If both 'race' and 'clan are None:
            Assigns a random race and a matching random clan.

        - If 'race' is None but 'clan' is set:
            Assigns the race that corresponds to the chosen clan.

        - If 'clan' is None but 'race' is set:
            Assigns a random clan from the chosen race.
        """

        if self.race is None and self.clan is None:
            self.race = random.choice(list(races.keys()))
            self.clan = random.choice(races[self.race])

        elif self.race is None and self.clan:
            for race, clan in races.items():
                if self.clan in clan:
                    self.race = race

        elif self.clan is None and self.race:
            for race, _clan in races.items():
                if self.race in race:
                    self.clan = random.choice(races[self.race])

    def random_gender(self):
        """Selects a random gender"""

        self.gender = random.choice(genders)

    def random_starting_class(self):
        """
        Randomizes the character class and/or specialization
        based on current attribute values.

        - If 'starting_class' and 'specialization' are None:
            Assigns a random class and then a random corresponding
            specialization.

        - If 'specialization' is None but 'starting_class' is set:
            Assigns a random specialization that belongs to the set class.

        - If 'starting_class' is None but 'specialization' is set:
            Assigns a random class that belongs to the set specialization.
        """

        if self.specialization is None and self.starting_class is None:
            self.starting_class = random.choice(starting_classes)

            for specialization, classes in specializations.items():
                if self.starting_class in classes:
                    self.specialization = specialization

        elif self.specialization is None and self.starting_class:

            for specialization, classes in specializations.items():
                if self.starting_class in classes:
                    self.specialization = specialization
                    print(self.specialization)

        elif self.starting_class is None and self.specialization:
            for _specialization, _classes in specializations.items():
                if self.specialization in specializations:
                    self.starting_class = random.choice(
                        specializations[self.specialization]
                    )

    def random_deity(self):
        """Selects a random patron"""

        self.deity = random.choice(deities)

    def random_specialization(self):
        """Selects a random specialization"""

        self.specialization = random.choice(list(specializations.keys()))

    def display_character(self):
        """Displays the character with the given settings"""

        print("\nYour New Character:")
        print(
            f"\n\tRace: {new_character.race}\n"
            f"\tClan: {new_character.clan}\n"
            f"\tGender: {new_character.gender}\n"
            f"\tDeity: {new_character.deity}\n"
            f"\tSpecialization: {new_character.specialization}\n"
            f"\tStarting Class: {new_character.starting_class}\n"
        )


races = {
    "Hyur": ["Midlander", "Highlander"],
    "Elezen": ["Wildwood", "Duskwight"],
    "Lalafell": ["Plainsfolk", "Dunesfolk"],
    "Miqo'te": ["Seekers of Sun", "Keeper of the Moon"],
    "Roegadyn": ["Sea Wolves", "Hellsguard"],
    "Au Ra": ["Xaela", "Raen"],
    "Hrothgar": ["Helions", "The Lost"],
    "Viera": ["Rava", "Veena"],
}

genders = (
    "Male",
    "Female",
)

starting_classes = (
    "Gladiator",
    "Marauder",
    "Lancer",
    "Archer",
    "Arcanist",
    "Conjurer",
    "Thaumaturge",
    "Pugilist",
)

deities = (
    "Halone",
    "Menphina",
    "Thaliak",
    "Nymeia",
    "Llymlaen",
    "Oschon",
    "Byregot",
    "Rhalgr",
    "Azeyma",
    "Nald'thal",
    "Nophica",
    "Althyk",
)

specializations = {
    "Tank": ["Marauder", "Gladiator"],
    "Melee DPS": ["Lancer", "Pugilist"],
    "Ranged Physical DPS": "Archer",
    "Ranged Magic DPS": ["Thaumaturge", "Arcanist"],
    "Healer": "Conjurer",
}


print(
    "Welcome to the FFXIV Character Creator Randomizer!\n\n"
    "Please select as many or as little options as you wish.\n"
    "Please type 'quit' to quit at any time.\n"
)


while main:
    print(
        "Please select one of the following options by their number:\n\n"
        "[1] Randomize everything\n"
        "[2] custom Randomization\n"
    )
    answer = input("Option: ").strip()

    if answer == "1":

        new_character = Character()

        new_character.random_race()
        new_character.random_gender()
        new_character.random_starting_class()
        new_character.random_deity()

        new_character.display_character()

        input("Press 'ENTER' to quit")
        quit()

    elif answer == "2":
        new_character = Character()

        while sub_main:
            print("\nFor the following options please respond with [Yes/No]\n")

            while race_clan_selection:
                answer = input("Would you like to randomize your race?: "
                               ).strip().lower()

                if answer == "yes":
                    answer = input(
                        "Would you like to also randomize your clan?: "
                                   ).strip().lower()

                    if answer == "yes":
                        new_character.random_race()
                        print("\nYour race and clan has been randomized!\n")
                        race_clan_deactivation()

                    elif answer == "no":
                        new_character.race = random.choice(list(races.keys()))
                        print(
                            f"\nYou got {new_character.race}!\n"
                            "\nYou can choose from the following clans: \n"
                        )

                        for race, clans in races.items():
                            if new_character.race in race:
                                for clan in clans:
                                    print(f"\t-{clan}")

                        clan = input(
                            "\nPlease enter the name of the "
                            "clan you would like to choose:\n"
                        ).strip()

                        new_character.clan = clan

                        print(f"\nYou chose {new_character.clan} "
                              f"from {new_character.race}\n"
                              )

                        race_clan_deactivation()

                    elif answer == "quit":
                        quit()

                elif answer == "no":
                    answer = input("Would you like to randomize a clan?: "
                                   ).strip().lower()

                    if answer == "yes":
                        print(
                            "\nWhich of the following races would you like?:\n"
                            )

                        n = 1

                        for race in list(races.keys()):
                            print(f"[{n}] {race}\n")
                            n += 1

                        race = input("Option: ").strip()
                        print("\n")

                        if race == "1":
                            new_character.race = "Hyur"

                        elif race == "2":
                            new_character.race = "Elezen"

                        elif race == "3":
                            new_character.race = "Lalafell"

                        elif race == "4":
                            new_character.race = "Miqo'te"

                        elif race == "5":
                            new_character.race = "Roegadyn"

                        elif race == "6":
                            new_character.race = "Au Ra"

                        elif race == "7":
                            new_character.race = "Hrothgar"

                        elif race == "8":
                            new_character.race = "Viera"

                        new_character.random_race()

                        print(
                            f"You chose {new_character.race} and were "
                            "given one of their clans at random.\n"
                              )

                        race_clan_deactivation()

                    elif answer == "no":
                        print(
                            "\nWhich of the following races would you like?:\n"
                            )

                        n = 1

                        for race in list(races.keys()):
                            print(f"[{n}] {race}\n")
                            n += 1

                        race = input("Option: ").strip()
                        print("\n")

                        if race == "1":
                            new_character.race = "Hyur"

                        elif race == "2":
                            new_character.race = "Elezen"

                        elif race == "3":
                            new_character.race = "Lalafell"

                        elif race == "4":
                            new_character.race = "Miqo'te"

                        elif race == "5":
                            new_character.race = "Roegadyn"

                        elif race == "6":
                            new_character.race = "Au Ra"

                        elif race == "7":
                            new_character.race = "Hrothgar"

                        elif race == "8":
                            new_character.race = "Viera"

                        print(f"\nYou chose {new_character.race}.\n")
                        print("\nYou can choose from the following clans: \n")

                        for race, clans in races.items():
                            if new_character.race in race:
                                for clan in clans:
                                    print(f"\t-{clan}")

                        clan = input(
                            "\nPlease enter the name of the "
                            "clan you would like to choose:\n"
                        ).strip()

                        new_character.clan = clan

                        print(
                            f"\nYou chose {new_character.clan} from "
                            f"the {new_character.race} race.\n"
                        )

                        race_clan_deactivation()

                elif answer == "quit":
                    quit()

                else:
                    error_prompt()
                    break

            while gender_selection:
                gender = input("Would you like to randomize your gender?: "
                               ).strip().lower()

                if gender == "yes":

                    new_character.random_gender()

                    print("\nGender has been randomized!\n")

                    gender_selection_deactivation()

                elif gender == "no":
                    print("\nPlease select one of the following options:\n")

                    for gender in genders:
                        print(f"\t-{gender}")

                    print("\n")
                    gender = input("Option: ").strip().title()

                    new_character.gender = gender

                    print(f"You chose {new_character.gender}.")

                    gender_selection_deactivation()

                elif gender == "quit":
                    quit()

                else:
                    error_prompt()

            while class_specialization_selection:
                starting_class = input(
                    "Would you like to randomize your starting class?: "
                    ).strip().lower()

                if starting_class == "yes":
                    specialization = input(
                        "\nWould you like to randomize your specialization?: "
                        ).strip().lower()

                    if specialization == "yes":

                        new_character.random_starting_class()

                        print(
                            "\nYour class and specialization has been "
                            "randomized.\n")

                        class_specialization_deactivation()

                    elif specialization == "no":
                        print("\nPlease choose from the following options:\n")

                        for specialization in specializations:
                            print(f"-{specialization}")

                        print("\n")
                        specialization = input("Option: ").strip()
                        print(
                            "\nYour starting class has been randomized.\n"
                              )

                        new_character.specialization = specialization

                        new_character.random_starting_class()

                        class_specialization_deactivation()

                elif starting_class == "no":
                    print(
                        "\nPlease choose one of the "
                        "following starting classes:\n"
                        )

                    for classes in starting_classes:
                        print(f"\t-{classes}")

                    print("\n")
                    starting_class = input("Option: ").strip().capitalize()

                    new_character.starting_class = starting_class

                    print(f"\nYou chose {new_character.starting_class}\n")

                    new_character.random_starting_class()

                    class_specialization_deactivation()

                elif starting_class == "quit":
                    quit()

                else:
                    error_prompt()

            while deity_selection:
                deity = input("Would you like to randomize your deity?: "
                              ).strip().lower()

                if deity == "yes":

                    new_character.random_deity()

                    print("\nYour deity has been randomized!\n")

                    deity_selection_deactivation()

                elif deity == "no":
                    print("\nPlease choose one of the following deities:\n")

                    for deity in deities:
                        print(f"\t-{deity}")

                    print("\n")
                    deity = input("Option: ").strip().capitalize()

                    new_character.deity = deity

                    print(f"You chose {new_character.deity}")

                    deity_selection_deactivation()

                elif deity == "quit":
                    quit()

                else:
                    error_prompt()

            while character_description:
                print(
                    "You have chosen all the options!\n"
                    "Here is your randomized character:\n"
                )

                new_character.display_character()

                input("Press 'ENTER' to quit")
                quit()

    elif answer == "quit":
        quit()

    else:
        error_prompt()
