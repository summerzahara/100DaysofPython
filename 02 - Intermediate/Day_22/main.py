from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turns animation off

# Create paddle
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

# Setup key listeners
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# Create Ball
ball = Ball()

# Create Scoreboard
scoreboard = Scoreboard()

game_active = True
while game_active:
    time.sleep(ball.level) # slows down movement
    screen.update()  # Turns on the screen
    ball.move_ball()

    # Detect Collision with top and bottom
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_vert()

    # Detect Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_hor()

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.right_point()

    # Detect right paddle miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.left_point()

screen.exitonclick()
