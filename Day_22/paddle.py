from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    """
    Models a paddle that can move up and down with the arrows
    """

    def __init__(self, x_start, y_start):
        super().__init__()
        self.shape("square")
        self.penup()
        # Starts at 20 x 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.x_start = x_start
        self.y_start = y_start
        self.setpos(self.x_start, self.y_start)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(self.x_start, new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.setpos(self.x_start, new_y)
