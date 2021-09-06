from turtle import Turtle, Screen
import random
rafi = Turtle()
rafi.color("maroon")
rafi.shape("triangle")

color = ["maroon", "dark red", "brown", "firebrick", "medium purple", "light sky blue", "yellow", "midnight blue", "forest green"]

for shape in range (3,11):
    rafi.color(random.choice(color))
    for side in range(shape):
        rafi.forward(100)
        rafi.rt(360/shape)


screen = Screen()
screen.exitonclick()
