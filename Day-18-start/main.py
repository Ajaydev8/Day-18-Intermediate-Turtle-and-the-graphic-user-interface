from turtle import Turtle, Screen
import turtle as t
import random

# Getting hold of the turtle class
tim = Turtle()
# tim.shape("turtle")
t.colormode(255)
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
# creating random colors using rgb
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

# for x in range(3, 10):
#     length = 100
#     angle = 360
#     random_color = random_color()
#     goal = x
#     while goal != 0:
#         tim.color(random_color)
#         tim.forward(length)
#         tim.right(360/x)
#         goal -= 1

# Challenge 4: Draw a random walk.

is_on = True
random_list = [20, -20]
angle = [90, 180, 270, 360]

while is_on:
    tim.speed("fastest")
    random_number = random.choice(random_list)
    random_angle = random.choice(angle)
    tim.width(10)
    tim.setheading(random_angle)
    tim.color(random_color())
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
