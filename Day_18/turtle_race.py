from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["tomato", "tan1", "gold", "lightgreen", "lightblue", "slateblue1"]
user_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_active = False
my_turtles = []

y_axis = -120
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, y_axis)
    my_turtles.append(new_turtle)
    y_axis += 50

if bet:
    race_active = True

while race_active:
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            race_active = False
            winner = colors.index(turtle.pencolor())
            if winner == user_colors.index(bet):
                print(f"You've won! The {user_colors[winner]} turtle is the winner!")
            else:
                print(f"You've lost! The {user_colors[winner]} turtle is the winner!")
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()