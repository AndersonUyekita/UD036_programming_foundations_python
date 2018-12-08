##############################################################################################
#                                                                               VERSION: 1.0 #
#  Author:   Anderson Hitoshi Uyekita                                                        #
#  Course:   Programming Foundations with Python                                             #
#  COD:      nd036                                                                           #
#  Project:  Rename file                                                                     #
#  Lesson:   02                                                                              #
#  Date:     07/12/2018                                                                      #
#  Tags:     Udacity, Python                                                                 #
#                                                                                            #
##############################################################################################

# This python file aims to change the filename removing the number.

import os
import string

def rename_files():
    # (1) get file names from a folder
    list_files = os.listdir(r"C:\")
    print(list_files)

    # Save the Current Work Directory
    saved_path = os.getcwd()

    # Set a new Directory
    os.chdir(r"C:\")

    # (2) for each file, rename filename
    for name in list_files:
        os.rename(name,name.translate(None,"0123456789"))

    # Return the orignal Directory
    os.chdir(saved_path)

rename_files()
