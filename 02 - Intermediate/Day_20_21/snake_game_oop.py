from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Ultimate Snake Game")
screen.tracer(0)  # Turns off the tracer

# Create snake body
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect Collision with Food
    if snake.head.distance(food) < 12:
        food.refresh()
        snake.extend()
        scoreboard.display_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_active = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_active = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
