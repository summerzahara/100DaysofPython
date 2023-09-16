"""
w = forwards
s = backwards
a = counter-clockwise (left)
d = clockwise (right)
c = clear drawing
"""
from turtle import Turtle, Screen

peeta = Turtle()
screen = Screen()
peeta.speed("fastest")


def move_forward():
    peeta.forward(10)


def move_backward():
    peeta.backward(10)


def move_counter_clockwise():
    heading = peeta.heading() + 10
    peeta.setheading(heading)
    peeta.forward(10)


def move_clockwise():
    heading = peeta.heading() - 10
    peeta.setheading(heading)
    peeta.forward(10)

def clear_screen():
    peeta.setpos(0, 0)
    peeta.setheading(90)
    peeta.clear()



def etch():
    peeta.setheading(90)
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=move_counter_clockwise)
    screen.onkey(key="d", fun=move_clockwise)
    screen.onkey(key="c", fun=clear_screen)


etch()
screen.exitonclick()
