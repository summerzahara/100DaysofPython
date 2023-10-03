import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_mgr = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car
    car_mgr.generate_cars()
    car_mgr.move_cars()

    # Detect collision with car
    for car in car_mgr.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.lost_game()

    # Detect successful run
    if player.finished_level():
        player.restart_run()
        car_mgr.level_up()
        scoreboard.increment_level()

screen.exitonclick()
