from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()# прячем черепаху и будет видно только итоговый результат написанного
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(x=-100, y=200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(x=100, y=200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over", align=ALIGN, font=FONT)

    def increase_score_l_paddle(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def increase_score_r_paddle(self):
        self.r_score += 1
        self.clear()
        self.update_score()