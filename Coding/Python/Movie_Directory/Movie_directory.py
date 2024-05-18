#Movie Directory Program

#Imported Modules
import sys

#Movie Directory
movie_list = []

#Defining start_of_code function
def start_of_code():
    while True:
        answer = input("Will that be all? (Y/N): ").strip().upper()

        if answer in ["Y", "YES"]:
            sys.exit()

        elif answer in ["N", "NO"]:
            break

        else:    
            print("Please enter a valid option.")
            start_of_code()

while True:

    user_input = input("Would you like to (View/Add/Remove/Exit): ").strip().title()

    #User wishes to view their directory
    if user_input in ["View", "V"]:

        answer = input("Would you like to view the whole directory or a specific movie by index number? (Whole/Index): ").strip().title()

        #Displays the whole movie_list
        if answer in ["Whole", "W"]:

            for movies in movie_list:
                print(f"<{movies}>")
            start_of_code()

        elif answer in ["Index", "I"]:
            while True:

                #Displays the selected movie by it's index
                try:
                    movie_index_number = int(input("Please enter the index number of the movie you would like to view: "))

                    print({movie_list[movie_index_number]})
                    start_of_code()

                #Catches invalid entries    
                except IndexError:
                    print("Invalid index number has been entered.")
                    break

    #User wishes to add a movie to the directory
    elif user_input in ["Add", "A"]:

        movie_name = input("Title: ")
        director_name = input("Director: ")
        release_year = input("Release Year?: ")
        movie_budget = input("Budget: ")

        #Adding all user variables into a single variable, formating them and appending them into the directory
        new_entry = (movie_name.strip().title(), director_name.strip().title(), release_year.strip(), movie_budget.strip())
        movie_list.append(new_entry)

        print(f"<{new_entry[0]}> has been added to the directory!")
        start_of_code()



    #elif statement if the user wishes to remove a movie
    elif user_input in ["Remove", "R"]:

        while True:
            try:
                removed_movie_index = int(input("What is the index number of the movie you would like to remove?: "))
                #removed_movie_index = int(removed_movie_index)

                print(f"Movie: {movie_list[removed_movie_index][0]} has been deleted!")

                removed_movie_index = int(removed_movie_index)

                del movie_list[removed_movie_index]
                start_of_code()

            except IndexError:
                print("Invalid index number has been entered.")
                break


    elif user_input in ["Exit", "E"]:
        sys.exit()

    #else statement to catch any invalid key entries
    else:
        print("Please enter a valid option.")
        continue