import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
status = True
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
num = 0
while num < 10:
    time.sleep(0.5)
    screen.update()
    car_manager.create_car()
    car_manager.moving_forward()

screen.exitonclick()