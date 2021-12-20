import time
from turtle import Screen
from player import Player
from car import Car
from level import Level


def game():
    level = Level()
    player = Player()
    car = Car()
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    screen.listen()
    screen.onkeypress(player.up, "Up")
    screen.onkey(reset, "space")
    screen.onkey(level.close, "Escape")

    loop_number = 0
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        level.scoreboard()

        # Create new cars every 5 times of loop
        if loop_number % 5 == 0:
            car.creator()

        car.move()

        # Increase speed when level up
        if player.ycor() >= 300:
            player.player_location()
            level.next_level()
            car.inc_speed()

        # Detects the collision and tell the user that game is over
        for cars in car.car_list:
            if player.distance(cars) < 20:
                level.over()
                game_is_on = False

        loop_number += 1


    screen.exitonclick()


def reset():
    Screen().clear()
    game()


game()
