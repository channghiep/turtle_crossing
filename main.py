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

game_is_on= True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.moving_forward()

    #Detect car hit
    for car in car_manager.cars[:]:
        if player.distance(car) < 10:
            print("hit")
            game_is_on = False

    #Detect win

    if player.ycor() > 280:
        print("win")

screen.exitonclick()