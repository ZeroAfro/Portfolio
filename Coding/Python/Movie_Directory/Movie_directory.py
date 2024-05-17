#Movie Directory Program

#Imported Modules
import sys

#Movie Directory
movie_list = [
  (   
  )
]

#Defining start_of_code to catch 'else' statments
def start_of_code():
    while True:
        answer = input("Will that be all? (Y/N): ")

        #if statement checking if the user is done or not
        if answer == "Y":
            sys.exit()

        elif answer == "N":
            break

        else:    
            print("Please enter a valid option.")
            start_of_code()

while True:

    #Requesting user input to check against if/elif statments
    user_input = input("Would you like to (View/Add/Remove/Exit): ")

    #elif alowing them to view movies based on index number
    if user_input == "View":

        answer = input("Would you like to view the whole directory or a specific movie by index number? (Whole/Index): ")

        if answer == "Whole":
            print(movie_list)
            start_of_code()

        elif answer == "Index":

                movie_index_number = int(input("Please type the index number of the movie you would like to view: "))

                print({movie_list[movie_index_number]})
                start_of_code()

    #User wishes to add a movie to the directory
    elif user_input == "Add":

        movie_name = input("Title: ")
        director_name = input("Director: ")
        release_year = input("Release Year?: ")
        movie_budget = input("Budget: ")

        #Adding all user variables into a single variable, formating them and appending them into the directory
        new_entry = (movie_name.strip().title(), director_name.strip().title(), release_year.strip(), movie_budget.strip())
        movie_list.append(new_entry)

        print(f"<{new_entry[0]}> has been added to the directory!")
        start_of_code()



    #elif statement if the user wished to remove a movie
    elif user_input == "Remove":
        
        while True:
            try:
                removed_movie_index = int(input("What is the index number of the movie you would like to remove?: "))
                #removed_movie_index = int(removed_movie_index)

                print(f"Movie: {movie_list[removed_movie_index][0]} has been deleted!")

                removed_movie_index = int(removed_movie_index)

                del movie_list[removed_movie_index]
                start_of_code()
            except IndexError:
                print("Invalid index number has been entered, try again.")
            

    elif user_input == "Exit":
        sys.exit()

    #else statement to catch any invalid key entries
    else:
        print("Please enter a valid option.")
        continue
