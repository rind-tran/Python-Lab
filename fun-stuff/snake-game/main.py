from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard



def main():
    game_is_on = True
    my_snake = Snake()
    my_food = Food()
    my_scoreboard = Scoreboard()
    screen = Screen()
    screen.tracer(0)
    screen.bgcolor("black")
    screen.listen()
    screen.onkey(key="Up", fun=my_snake.up)
    screen.onkey(key="Down", fun=my_snake.down)
    screen.onkey(key="Left", fun=my_snake.left)
    screen.onkey(key="Right", fun=my_snake.right)

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        my_snake.move_snake()

        # Detect collision with food
        if my_snake.head.distance(my_food) < 15:
            my_food.refresh()
            my_scoreboard.score += 1
            my_snake.extend()

        # Calculate and show score
        my_scoreboard.update_score()

        # Detect collision with wall
        if my_snake.head.xcor() > 300 or my_snake.head.xcor() < -300 or my_snake.head.ycor() > 300 or my_snake.head.ycor() < -300:
            game_is_on = False
            my_scoreboard.game_over()

        # Detect collision with wall
        for segment in my_snake.segments[3:]:
            if my_snake.head.distance(segment) < 10:
                game_is_on = False
                my_scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
