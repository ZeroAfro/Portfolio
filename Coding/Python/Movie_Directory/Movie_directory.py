#Movie Directory Program

#Imported Modules
import sys

#Place holder for directory
movie_list = []

#Function asking if they would like to continue
def continuation_confirmation():
    while True:
        answer = input("Will that be all? (Y/N): ").strip().lower()

        if answer in ["y", "yes"]:
            sys.exit()

        elif answer in ["n", "no"]:
            break

        else:    
            print("Please enter a valid option.")
            continuation_confirmation()

while True:

    user_input = input("Would you like to (View/Add/Remove/Exit): ").strip().lower()

    #User wishes to view their directory
    if user_input in ["v", "view"]:

        answer = input("Would you like to view the whole directory or a specific movie by index number? (Whole/Index): ").strip().lower()

        #Displays the whole movie_list
        if answer in ["w", "whole"]:

            for movies in movie_list:
                print(f"<{movies}>")
            continuation_confirmation()

        elif answer in ["i", "index"]:
            while True:

                #Displays the selected movie by it's index
                try:
                    movie_index_number = int(input("Please enter the index number of the movie you would like to view: "))

                    print({movie_list[movie_index_number]})
                    continuation_confirmation()

                #Catches invalid entries    
                except IndexError:
                    print("Invalid index number has been entered.")
                    break

    #User wishes to add a movie to the directory
    elif user_input in ["a", "add"]:

        movie_name = input("Title: ")
        director_name = input("Director: ")
        release_year = input("Release Year?: ")
        movie_budget = input("Budget: ")

        #Adding all user variables into a single variable, formating them and appending them into the directory
        new_entry = (movie_name.strip().title(), director_name.strip().title(), release_year.strip(), movie_budget.strip())
        movie_list.append(new_entry)

        print(f"<{new_entry[0]}> has been added to the directory!")
        continuation_confirmation()



    #elif statement if the user wishes to remove a movie
    elif user_input in ["r", "remove"]:

        while True:
            try:
                removed_movie_index = int(input("What is the index number of the movie you would like to remove?: "))
                #removed_movie_index = int(removed_movie_index)

                print(f"Movie: {movie_list[removed_movie_index][0]} has been deleted!")

                removed_movie_index = int(removed_movie_index)

                del movie_list[removed_movie_index]
                continuation_confirmation()

            except IndexError:
                print("Invalid index number has been entered.")
                break


    elif user_input in ["e", "exit"]:
        sys.exit()

    #else statement to catch any invalid key entries
    else:
        print("Please enter a valid option.")
        continue