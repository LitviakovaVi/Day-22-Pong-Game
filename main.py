from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
# настравиаем экран:
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# отключаем анимацию и делаем все действия за кулисами:
screen.tracer(0)
'''
задаем позицию для левого и правого ворот, тем самым мы получаем неожиданный аргумент,
который должны передать в класс:
'''
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# вызываем функцию, которая отвечает за управление с клавиатуры:
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()# прослушивает события холста
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move_ball()
    # detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_l_paddle()
    if ball.xcor() < -380:
        scoreboard.increase_score_r_paddle()
        ball.reset_position()

        # game_is_on = False

    # обновляем готовую картинку:
    screen.update()


screen.exitonclick()