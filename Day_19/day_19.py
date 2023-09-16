from turtle import Turtle, Screen

peeta = Turtle()
screen = Screen()

def move_forward():
    peeta.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()