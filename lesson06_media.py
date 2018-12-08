##############################################################################################
#                                                                               VERSION: 1.0 #
#  Author:   Anderson Hitoshi Uyekita                                                        #
#  Course:   Programming Foundations with Python                                             #
#  COD:      nd036                                                                           #
#  Project:  Send SMS Message                                                                #
#  Lesson:   06                                                                              #
#  Date:     07/12/2018                                                                      #
#  Tags:     Udacity, Python                                                                 #
#                                                                                            #
##############################################################################################

import webbrowser

# Creating a new Classself.
class Movie():   # Upper case to define the class (good practice)

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):   # Constructor
        self.title = movie_title                      #
        self.storyline = movie_storyline              # Defining the Instance Variables
        self.poster_image_url = poster_image          #
        self.trainer_youtube_url = trailer_youtube    #

    def show_trailer(self): # This is a method
        webbrowser.open(self.trainer_youtube_url)
