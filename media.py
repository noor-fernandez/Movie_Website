#############################
# Project 1: Movie Website
# Date Started: 01/15/2017
# Date Completed: 01/18/2017
# Project by: Noor Fernandez
#############################

########################################## Media File #########################################
# Description: This file creates the base class 'Movie' to allow for instances of this class
#              to be used in the entertainment_center.py file. Class definition and parameters
#              from the class Python Foundations on Udacity.
###############################################################################################
import webbrowser

class Movie(object):
    """Docstring for Movie. This class provides a way to store movie related information."""

# The super keyword in the __init__ function is useful for multiple inheritance
# should I choose to create a subclass to the baseclass 'Movie'
# and for future code refactoring

# I chose these variable definitions to match the variables named
# in the Udacity supplied fresh_tomatoes.py file
    def __init__(self, movie_title, movie_storyline,poster_image_url,trailer_youtube):
        super(Movie, self).__init__()
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

#Opens the youtube trailer on the fresh_tomatoes webpage
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
