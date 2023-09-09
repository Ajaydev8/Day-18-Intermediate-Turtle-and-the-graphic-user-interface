import colorgram

# Extraction  the colors from an image
colors = colorgram.extract('download.jpg', 50)
colors_list = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.g
    color_tuple = (r, g, b)
    colors_list.append(color_tuple)

print(colors_list)
