from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
# import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("DarkSlateGray")
screen.tracer(0)
screen.title("Feed the Snake")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def end_game():
    screen.bye()


screen.onkey(end_game, "Escape")

game_is_on = True


def update_screen():
    global game_is_on
    if game_is_on:
        screen.update()
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.increase_score()
            snake.extend()

        # Detect collision with wall
        if abs(snake.head.xcor()) > 240 or abs(snake.head.ycor()) > 240:
            score.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()

        screen.ontimer(update_screen, 100)  # Update the screen every 100ms


update_screen()

screen.mainloop()  # Keep the window open until the user closes it
