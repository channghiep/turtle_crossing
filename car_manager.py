from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.create_car()
    #     self.create_car()
    #
    #
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape = "square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            # new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.start_y = random.choice(list(range(-250,250)))
            new_car.start_x = 300
            new_car.goto(new_car.start_x, new_car.start_y)
            self.cars.append(new_car)
    def moving_forward(self):
        # for car_num in range(0,len(self.cars)-1):
        #     new_x = self.cars[car_num].xcor() - MOVE_INCREMENT
        #     # new_y = self.cars[car_num].ycor()
        #     self.cars[car_num].goto(new_x,self.cars[car_num].ycor())
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)