import webbrowser


class Movie(object):
    '''This class provides a way to store data related to movies.

    Attributes:
     title (str): Movie title.
     storyline (str): Movie plot.
     poster_image_url (str): Box art URL (or poster URL).
     trailer_youtube_url (str): A YouTube link to the movie trailer.
    '''
    # Class Variable, contains the standard ratings assigned by the MPAA
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
                self, movie_title, movie_storyline,
                movie_poster_image_url, movie_trailer_url):  # Constructor
        # Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_url

    def show_trailer(self):  # Instance Method
        webbrowser.open(self.trailer_youtube_url)
