import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

def main():
    screen = Screen()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)

    # Classes initialization
    snake = Snake()
    food = Food()
    score = ScoreBoard()

    # Key binds
    screen.listen()
    screen.onkey(snake.turn_north, "Up")
    screen.onkey(snake.turn_south, "Down")
    screen.onkey(snake.turn_east, "Right")
    screen.onkey(snake.turn_west, "Left")
    screen.onkey(main, "r")
    screen.onkey(screen.bye, "Escape")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.02)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 20:
            food.refresh()
            score.increase_score()
            snake.extend_snake()
        
        # Detect collision with the wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            score.game_over()
            game_is_on = False

        # Detect collision with itself - checking every segment except the head
        for segment in snake.segments[1::]:
            if snake.head.distance(segment) < 5:
                score.game_over()
                game_is_on = False

    screen.exitonclick()

if __name__ == "__main__":
    main()