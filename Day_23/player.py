from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.x_start = 0
        self.y_start = -280
        self.setpos(self.x_start, self.y_start)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(self.x_start, new_y)

    def finished_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def restart_run(self):
        self.setpos(self.x_start, self.y_start)

