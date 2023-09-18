from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Ultimate Snake Game")
screen.tracer(0)  # Turns off the tracer

# Create snake body
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_active = True
while game_active:
    screen.update()
    time.sleep(.1)
    snake.move_snake()

screen.exitonclick()
