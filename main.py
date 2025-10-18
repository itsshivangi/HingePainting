# import colorgram  This module is commented out because it requires an external library/package . You can uncomment and use it if you have the library installed.

# rgb_colors = []
# extracted_colors = colorgram.extract('hirst.jpg', 22)
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

import turtle as turtle_module
import random


screen = turtle_module.Screen()
turtle_module.colormode(255)



tim = turtle_module.Turtle()

tim.speed("fastest")

tim.penup()

tim.hideturtle()


colors = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (0, 255, 255),    # Cyan
    (255, 0, 255),    # Magenta
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 192, 203),  # Pink
    (139, 69, 19),    # Brown
    (0, 0, 0),        # Black
    (255, 255, 248),  # White
    (128, 128, 128),  # Gray
    (211, 211, 211),  # Light Gray
    (64, 64, 64),     # Dark Gray
    (0, 255, 0),      # Lime
    (0, 0, 128),      # Navy
    (128, 0, 0),      # Maroon
    (128, 128, 0),    # Olive
    (0, 128, 128),    # Teal
    (255, 215, 0),    # Gold
    (192, 192, 192)   # Silver
]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1,number_of_dots := 100 + 1):
    tim.dot(20,random.choice(colors))
    tim.forward(50)
    if dot_count % 10 == 0: 

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()


