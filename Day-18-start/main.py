from turtle import Turtle, Screen

# Getting hold of the turtle class
tim = Turtle()
# tim.shape("turtle")
tim.color("navy")
# timmy.forward(10)

# Challenge-1: Draw a square
# for turtle in range(4):
#     tim.forward(100)
#     tim.right(90)


# Challenge-2: Draw dashed lines
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Challenge-3: Draw different shapes
turtle_colors = ["#FF6B6B", "#6BFF6B", "#6B6BFF", "#FFD700", "#FF69B4", "#BA55D3", "#87CEEB", "#F08080", "#20B2AA", "#FFA07A"]

# for x in range(3, 10):
#     color = turtle_colors[x]
#     length = 100
#     angle = 360
#     goal = x
#     while goal != 0:
#         tim.color(color)
#         tim.forward(length)
#         tim.right(360/x)
#         goal -= 1

# Challenge 4: Draw a random walk.
import random
is_on = True
random_list = [20, -20]
angle = [90, 180, 270, 360]

while is_on:
    tim.speed("fastest")
    random_number = random.choice(random_list)
    random_color = random.choice(turtle_colors)
    random_angle = random.choice(angle)
    tim.width(10)
    tim.setheading(random_angle)
    tim.color(random_color)
    tim.forward(random_number)


# How to alias module

# import turtle as t

# What it does is whenever you write a turtle you just have to write t
# Sometimes there are modules which have very long name so this method works just fine for it
# tim = t.Turtle()

# Importing new modules
# Pycharm allows to download directly from the IDE which is great
import heroes

hero = heroes.gen()
print(hero)


# Getting hold of the screen
screen = Screen()
# This will prevent the screen from closing, It is only closed when clicked
screen.exitonclick()
