from turtle import Screen
import turtle as t
import random
rafi = t.Turtle()
rafi.color("maroon")
rafi.shape("triangle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    the_tuple = (r, g, b)
    return the_tuple


rafi.speed(0)

for _ in range(120):
    rafi.circle(100)
    rafi.lt(_*2)
    rafi.color(random_color())

angle = ["0", "90", "180", "270"]
rafi.width(15)

for shape in range (3,11):
    rafi.color(random_color())
    for side in range(shape):
        rafi.forward(100)
        rafi.rt(360/shape)


for _ in range(1000):
    rafi.forward(30)
    m_angle = int(random.choice(angle))
    rafi.setheading(m_angle)
    rafi.color(random_color())




screen = Screen()
screen.exitonclick()
