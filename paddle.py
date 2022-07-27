from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):# передаем неожиданный аргумент position
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)# при каждом движении ворота будут перемещаться на расстояние + 20 (вверх)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)# при каждом движении ворота будут перемещаться на расстояние - 20(вниз)


