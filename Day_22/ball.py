from turtle import Turtle

MOVE_DISTANCE = 20


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        # self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.level = 0.1

    def move_ball(self):
        # self.setheading(45)
        # self.forward(MOVE_DISTANCE)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce_vert(self):
        self.y_move *= -1

    def bounce_hor(self):
        self.x_move *= -1
        self.level *= 0.9

    def reset(self):
        self.setpos(0, 0)
        self.level = 0.1
        self.bounce_hor()
