import colorgram 
import turtle as t
import random

t.colormode(255)

colors = colorgram.extract("hirst.jpg", 30)

def draw_line_of_dots():
    counter = 0 
    while counter < 10:
        random_color = random.choice(color_list)
        tim.dot(50, random_color)
        tim.forward(130)
        counter +=1

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

# rgb_color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r,g,b)

#     rgb_color_list.append(new_colour)


# print(rgb_color_list)

color_list = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]
tim = t.Turtle()
tim.shape("arrow")

for num in range (-5, 6):
    tim.penup()
    y_axis = num * 100
    tim.setposition (-600, y_axis)
    draw_line_of_dots()
    

screen = t.Screen()
screen.exitonclick()