class Movie:
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


my_movie = Movie('Some title', '1997', 'English', '4.5')
print('Title of the movie is:', my_movie.title)
print('Year of the movie is:', my_movie.year)
print('Language of the movie is:', my_movie.language)
print('Rating of the movie is:', my_movie.rating)
