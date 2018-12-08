##############################################################################################
#                                                                               VERSION: 1.0 #
#  Author:   Anderson Hitoshi Uyekita                                                        #
#  Course:   Programming Foundations with Python                                             #
#  COD:      nd036                                                                           #
#  Project:  Mindstorms                                                                      #
#  Lesson:   03                                                                              #
#  Date:     07/12/2018                                                                      #
#  Tags:     Udacity, Python                                                                 #
#                                                                                            #
##############################################################################################

import turtle

def draw_square():
    # Open a screen to draw something
    window = turtle.Screen()

    # Defining the background color
    window.bgcolor("red")

    # Creating the object and assign to a variable
    brad = turtle.Turtle()

    # Modify the format of the Turtle
    brad.shape("turtle")

    # Modify the turtle color
    brad.color("green")

    # Speed up the turtle!! =)
    brad.speed(2)

    brad.forward(100)  # Move 100 units foward
    brad.right(90)     # Turn 90 degrees (clockwise)
    brad.forward(100)  # Move 100 units foward
    brad.right(90)     # Turn 90 degrees (clockwise)
    brad.forward(100)  # Move 100 units foward
    brad.right(90)     # Turn 90 degrees (clockwise)
    brad.forward(100)  # Move 100 units foward
    brad.right(90)     # Turn 90 degrees (clockwise)

    # Close the windows after a click
    window.exitonclick()

draw_square()
