##############################################################################################
#                                                                               VERSION: 1.0 #
#  Author:   Anderson Hitoshi Uyekita                                                        #
#  Course:   Programming Foundations with Python                                             #
#  COD:      nd036                                                                           #
#  Project:  Send SMS Message                                                                #
#  Lesson:   05                                                                              #
#  Date:     07/12/2018                                                                      #
#  Tags:     Udacity, Python                                                                 #
#                                                                                            #
##############################################################################################

import urllib.request

# This function load a txt
def read_text():
    """
    This functions load the movie_quotes.txt file
    The output is a list.
    """
    # Load the txt
    quotes = open("movie_quotes.txt")

    # Convert the quotes into list
    contents_of_file = quotes.read()

    # Print the converted quotes
    print(contents_of_file)

    # Close the open file
    quotes.close()

    # Run the check profanity
    check_profanity(contents_of_file)



# This function check a cursed word in www.wdylike.appspot.com/?q=
def check_profanity(text_to_check):
    """
    This function access the internet to check if any word of a variable is cursed.
    """
    # Connect to the wdylike website
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)

    # convert the result in list
    output = connection.read()

    # print
    print(connection)

    # close connection
    connection.close()



read_text()
