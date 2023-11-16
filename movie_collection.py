# movie_collection.py

import requests

class MovieCollection:
    def __init__(self, api_key):
        self.api_key = api_key
        self.movies = self.fetch_movies()

    def fetch_movies(self):
        base_url = "https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": self.api_key,
            "language": "en-US",
            "with_genres": "28",  # Genre ID for Action movies
            "page": 1,
            "total_pages": 10,  # Fetch 500 movies (50 per page)
        }

        movies = []

        for page in range(1, params["total_pages"] + 1):
            params["page"] = page
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                page_movies = data.get("results", [])
                movies.extend(page_movies)

        return movies

    def get_random_movie(self):
        if self.movies:
            return self.movies.pop()
        else:
            return None
