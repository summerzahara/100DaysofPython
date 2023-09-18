from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Ultimate Snake Game")
screen.tracer(0) #Turns off the tracer

# Create snake body

segments = []

x_pos = 0
y_pos = 0
for n in range(3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.setpos(x_pos, y_pos)
    segments.append(snake)
    x_pos -= 20

# Move the snake
game_active = True
while game_active:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].setpos(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()