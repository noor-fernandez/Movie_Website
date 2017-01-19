import webbrowser #This imports the module webbrowser used in the second function 'show_trailer'

class Movie(object):
    """Docstring for Movie. This class provides a way to store movie related information.""" #In-function documentation

    def __init__(self, movie_title, movie_storyline,poster_image_url,trailer_youtube): #init function for class 'Movie'
        super(Movie, self).__init__() #The super keyword is useful for multiple inheritance should I choose
        self.title = movie_title      #to create a subclass to the baseclass 'Movie' and future code refactoring
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube #These are all the parameters for the init function

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) #Opens the youtube trailer on the fresh_tomatoes webpage
