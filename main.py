import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect collision with the upper wall
    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.level_up()
        score_board.update_score()



screen.exitonclick()
