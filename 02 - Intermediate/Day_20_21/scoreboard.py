from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over.", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def display_score(self):
        self.score += 1
        self.update_scoreboard()
