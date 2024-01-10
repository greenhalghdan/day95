from turtle import  Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 1

    def move_bullet(self):
        # new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(self.ycor(), new_y)
        self.move_speed *= 0.9


