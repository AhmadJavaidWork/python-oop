class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title


my_movie = Movie('The Godfather', 4.8)

print(my_movie.get_title())
