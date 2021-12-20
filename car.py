from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car:

    def __init__(self):
        self.car_list = []
        self.move_distance = 5


    def creator(self):
        y_position = random.randint(-230, 250)
        car_block = Turtle()
        car_block.penup()
        car_block.setheading(180)
        car_block.color(random.choice(COLORS))
        car_block.shape("square")
        car_block.turtlesize(stretch_wid=1, stretch_len=2)
        car_block.goto(300, y_position)
        self.car_list.append(car_block)


    def move(self):
        for car in self.car_list:
            car.forward(self.move_distance)

            if car.xcor() < -300:
                car.hideturtle()


    def inc_speed(self):
        self.move_distance += 5
