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

# Splitting the code into two

import turtle

def draw_square(any_turtle):     # This functions works for any turtle
    while True:
        for i in range(1,5):
            any_turtle.forward(100)  # Move 100 units foward
            if i == 4:
                any_turtle.right(90 + 20)     # Turn 90 degrees (clockwise)
            else:
                any_turtle.right(90)
def draw_art():
    # Open a screen to draw something
    window = turtle.Screen()

    # Defining the background color
    window.bgcolor("gray")

    # Creating the object and assign to a variable
    brad = turtle.Turtle() # Brad born

    # Modify the format of the Turtle
    brad.shape("turtle")

    # Modify the turtle color
    brad.color("green")

    # Speed up the turtle!! =)
    brad.speed(2)

    # Call function to Brad draw a square
    draw_square(brad)

    # Close the windows after a click
    window.exitonclick()


draw_art()
