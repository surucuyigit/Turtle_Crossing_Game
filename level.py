import turtle
from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.num_of_level = 1
        self.scoreboard()


    def scoreboard(self):
        self.goto(-280, 250)
        self.write(f"Level: {self.num_of_level}", align="left", font=FONT)

    def next_level(self):
        self.clear()
        self.num_of_level += 1


    def over(self):
        self.home()
        self.write("Game Over!", align="center", font=FONT)


    def close(self):
        turtle.bye()

