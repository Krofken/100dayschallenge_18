import colorgram
import random
from turtle import Screen
import turtle as turtle_module

#rgb_colors = []
#colors = colorgram.extract('hist spot painting.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    _tuple = (r, g, b)
#    rgb_colors.append(_tuple)




turtle_module.colormode(255)
color_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]

screen = Screen()

rafi = turtle_module.Turtle()
rafi.penup()
rafi.hideturtle()
rafi.speed(0)

x_cor = -225
y_cor = -250
for _ in range(1, 11):
    rafi.setpos(x_cor, y_cor)
    y_cor += 50
    for x in range(10):
        rafi.color(random.choice(color_list))
        rafi.dot(20)
        rafi.forward(50)

screen.exitonclick()
