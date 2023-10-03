import random
import turtle
import turtle as t
from turtle import Turtle

t.colormode(255)
timmy = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

direction = [0, 90, 180, 270]
def random_walk_two():
    timmy.pensize(10)
    timmy.speed("fastest")
    for n in range(200):
        timmy.color(random_color())
        timmy.forward(25)
        timmy.setheading(random.choice(direction))

def spiralgraph(gap):
    timmy.pensize(2)
    timmy.speed("fastest")
    for n in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)
        print(timmy.heading())




spiralgraph(5)