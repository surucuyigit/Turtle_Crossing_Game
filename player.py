from turtle import Turtle
PLAYER_LOCATION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.move_speed = 10
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.player_location()

    def player_location(self):
        self.goto(PLAYER_LOCATION)

    def up(self):
        self.forward(self.move_speed)


