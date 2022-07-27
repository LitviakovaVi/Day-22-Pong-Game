from turtle import Turtle
import random

class Ball(Turtle):# наследуем класс от черепахи
    def __init__(self):
        super().__init__()
        self.shape("circle")# задаем форму круга
        self.shapesize(stretch_wid=1, stretch_len=1)# задаем диаметр мячика
        self.color("red")# задаем цвет мячика
        self.penup()# поднимаем ручку вверх? чтобы не отрисовывать перемещение мячика
        # self.goto(0, 0)# размещаем мячик по центру окна
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 #устанавливаю скорость движения мяча через тайм слип

    def move_ball(self):
        new_x = self.xcor() + self.x_move # добавляем сумму отклонения к координатам, чтобы переместить мяч (чтобы движение бело вверх)
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 # меняем сумму отклонения Y на противоположную, чтобы вычесть ее от координат
        # (чтобы движение бело вниз), когда мяч отскакивает от стены сверху
        self.move_speed -= 0.01

    def bounce_x(self):
        self.x_move *= -1 # меняем сумму отклонения X на противоположную, чтобы вычесть ее от координат
        # (чтобы движение бело влево), когда мяч отскакивает от правых ворот
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()






