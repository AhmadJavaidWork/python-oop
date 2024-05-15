class Movie:
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


myMovie = Movie('Some title', '1997', 'English', '4.5')
print('Title of the movie is:', myMovie.title)
print('Year of the movie is:', myMovie.year)
print('Language of the movie is:', myMovie.language)
print('Rating of the movie is:', myMovie.rating)
