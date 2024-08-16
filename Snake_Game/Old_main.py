from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("DarkSlateGray")
screen.title("Feed the Snake")
screen.tracer(0)

# segment_1 = Turtle("square")
# segment_1.color("white")
# segment_1.penup()
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.penup()
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.penup()
# segment_3.goto(-40, 0)

# Easier way:

# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for position in STARTING_POSITIONS:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # for seg_num in range(len(segments) - 1, 0, -1):  # Start, Stop, Step
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    #
    # segments[0].forward(20)
    snake.move()

screen.exitonclick()
