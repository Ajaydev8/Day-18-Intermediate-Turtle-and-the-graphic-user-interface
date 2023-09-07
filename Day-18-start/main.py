# from turtle import Turtle, Screen
#
# # Getting hold of the turtle class
# tim = Turtle()
# tim.shape("turtle")
# tim.color("navy")
# # timmy.forward(10)
#
# # Challenge-1: Draw a square
# for turtle in range(4):
#     tim.forward(100)
#     tim.right(90)

# How to alias module

import turtle as t

# What it does is whenever you write a turtle you just have to write t
# Sometimes there are modules which have very long name so this method works just fine for it
tim = t.Turtle()






# Getting hold of the screen
screen = Screen()
# This will prevent the screen from closing, It is only closed when clicked
screen.exitonclick()
