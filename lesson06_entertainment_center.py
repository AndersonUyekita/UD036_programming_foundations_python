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

import lesson06_media

# Creating a object
godfather = lesson06_media.Movie("The Godfather",
                                "The Godfather is a 1972 American crime film directed by Francis Ford Coppola and produced by Albert S. Ruddy, based on Mario Puzo's best-selling novel of the same name. It stars Marlon Brando and Al Pacino as the leaders of a fictional New York crime family. The story, spanning 1945 to 1955, chronicles the family under the patriarch Vito Corleone (Brando), focusing on the transformation of Michael Corleone (Pacino) from reluctant family outsider to ruthless mafia boss.",
                                "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                                "https://www.youtube.com/watch?v=i96VS_z8y7g")

# Print the storyline
print(godfather.storyline)

# Print the title
print(godfather.title)

# Print the image
print(godfather.poster_image_url)

# Print the youtube link
print(godfather.trainer_youtube_url)

# Creating other object
et_the_terrestrial = lesson06_media.Movie("E.T. the Extra-Terrestrial",
                                          "E.T. the Extra-Terrestrial is a 1982 American science fiction film produced and directed by Steven Spielberg, and written by Melissa Mathison.",
                                          "https://en.wikipedia.org/wiki/E.T._the_Extra-Terrestrial#/media/File:E_t_the_extra_terrestrial_ver3.jpg",
                                          "https://www.youtube.com/watch?v=qYAETtIIClk")

# Print the storyline
print(et_the_terrestrial.storyline)

# Print the title
print(et_the_terrestrial.title)

# Print the image
print(et_the_terrestrial.poster_image_url)

# Print the youtube link
print(et_the_terrestrial.trainer_youtube_url)

# Open a browser and play the youtube trailer!
godfather.show_trailer() # Its works!! =)
