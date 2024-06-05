# Movie Directory Program

# Library Imports
from sys import exit

# Place holder for directory
movie_list = []


# Function asking if they would like to continue
def exit_prompt():
    while True:
        answer = input("Will that be all? (Y/N): ").strip().lower()

        if answer in ["y", "yes"]:
            exit()
        elif answer in ["n", "no"]:
            break
        else:
            print("Please enter a valid option.")
            exit_prompt()


while True:

    user_input = input(
        "Would you like to (View/Add/Remove/Exit): "
        ).strip().lower()

    if user_input in ["v", "view"]:

        answer = input(
            "Would you like to view the whole directory or"
            " a specific movie by index number? (Whole/Index): "
            ).strip().lower()

        if answer in ["w", "whole"]:
            # For loop to interate through each movie and prints it
            for movies in movie_list:
                print(f"<{movies}>")
            exit_prompt()

        elif answer in ["i", "index"]:
            while True:

                try:
                    movie_index_number = int(
                        input(
                            "Please enter the index number"
                            " of the movie you would like to view: "
                            )
                        )
                    print({movie_list[movie_index_number]})
                    exit_prompt()
                except IndexError:
                    print("Invalid index number has been entered.")
                    break

    elif user_input in ["a", "add"]:

        movie_name = input("Title: ")
        director_name = input("Director: ")
        release_year = input("Release Year?: ")
        movie_budget = input("Budget: ")

        # Takes user inputs and formats them for the list
        new_entry = (
                    movie_name.strip().title(),
                    director_name.strip().title(),
                    release_year.strip(),
                    movie_budget.strip()
                    )
        movie_list.append(new_entry)

        print(f"<{new_entry[0]}> has been added to the directory!")
        exit_prompt()

    elif user_input in ["r", "remove"]:

        while True:
            try:
                removed_movie_index = int(
                    input(
                        "What is the index number of"
                        " the movie you would like to remove?: "
                        )
                    )
                movie_title = movie_list[removed_movie_index][0]
                print(f"Movie: {movie_list} has been deleted!")
                removed_movie_index = int(removed_movie_index)
                del movie_list[removed_movie_index]
                exit_prompt()
            except IndexError:
                print("Invalid index number has been entered.")
                break

    elif user_input in ["e", "exit"]:
        exit()

    else:
        print("Please enter a valid option.")
        continue
