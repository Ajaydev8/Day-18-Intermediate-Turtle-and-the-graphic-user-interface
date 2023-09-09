import colorgram
from turtle import Turtle, Screen
import random

# Extraction  the colors from an image
colors = colorgram.extract('download.jpg', 30)
colors_list = []
screen = Screen()
tim = Turtle()


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.g
    color_tuple = (r, g, b)
    colors_list.append(color_tuple)

rgb_colors = [(236, 244, 244), (236, 224, 224), (197, 7, 7), (195, 164, 164), (201, 75, 75), (231, 54, 54),
              (110, 179, 179), (217, 163, 163), (27, 105, 105), (35, 186, 186), (19, 29, 29), (13, 23, 23),
              (212, 135, 135), (233, 223, 223), (199, 33, 33), (13, 183, 183), (230, 166, 166), (126, 189, 189),
              (8, 49, 49), (40, 132, 132), (128, 219, 219), (58, 12, 12), (67, 22, 22), (114, 90, 90), (146, 216, 216),
              (179, 17, 17), (233, 66, 66)]

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

tim.penup()
tim.goto(-250, -250)
tim.speed("fastest")

for _ in range(10):
    random_rgb_color = random.choice(rgb_colors)
    hex_color = rgb_to_hex(random_rgb_color)  # Convert RGB to Hex
    tim.color(hex_color)
    tim.dot(20)
    tim.forward(50)

screen.exitonclick()
