# main.py

from movie_collection import MovieCollection
def print_movie_details(movie):
    if movie:
        print("\nMovie Details:")
        print("Title:", movie.get("title"))
        print("Overview:", movie.get("overview"))
        print("Release Date:", movie.get("release_date"))
        print("Genre:", ", ".join(genre["name"] for genre in movie.get("genres", [])))
        print("Average Rating:", movie.get("vote_average"))
    else:
        print("No more English action movies in the collection.")

def main():
    api_key = '8ba6ba3527a0339e21a71bef9774ec66'
    print('Please wait while movies load...')
    movie_collection = MovieCollection(api_key)

    while True:
        user_choice = input("Enter 1 to print the next movie, 2 to exit: \n")

        if user_choice == "1":
            random_movie = movie_collection.get_random_movie()
            print_movie_details(random_movie)
        elif user_choice == "2":
            print("Thank you for letting us assist you, goodbye!")
            break
        else:
            print("Invalid input. Please enter 1 to print the next movie or 2 to exit.")

if __name__ == "__main__":
    main()
