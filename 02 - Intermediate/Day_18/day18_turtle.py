import tkinter
from turtle import Turtle, Screen
from tk_colors import colors
from random import choice

timmy = Turtle()
timmy.shape("arrow")
timmy.color("black")


def dotted_line():
    for n in range(50):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)


def square_to_decagon(sides):
    while sides < 11:
        angle = 360 / sides
        for n in range(sides):
            timmy.forward(100)
            timmy.right(angle)
        sides += 1
        timmy.pencolor(choice(colors))
        print(sides)
        print(angle)


def forward():
    timmy.forward(15)

def left():
    timmy.left(90)
    timmy.forward(15)

def right():
    timmy.right(90)
    timmy.forward(15)

def backwards():
    timmy.right(180)
    timmy.forward(15)

directions = [1, 2, 2, 4]

def random_walk():
    timmy.pensize(7)
    timmy.speed("fastest")
    for n in range(200):
        move = choice(directions)
        timmy.pencolor(choice(colors))
        if move == 1:
            forward()
        elif move == 2:
            left()
        elif move == 3:
            backwards()
        elif move == 4:
            right()


random_walk()



screen = Screen()
screen.exitonclick()
