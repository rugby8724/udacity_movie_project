import webbrowser


class Movie():
    """ This class provides a way to store movie related infomation"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """__init__ creates space in memory for a new object of the
           movie class """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """show_trailer opens a movie objects movie trailer"""
        
        webbrowser.open(self.trailer_youtube_url)
