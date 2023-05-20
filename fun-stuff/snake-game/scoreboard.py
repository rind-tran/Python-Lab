from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 315)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", move=False, align='center', font=('Arial', 25, 'normal'))
