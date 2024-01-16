from turtle import Turtle
from bullet import Bullet
import threading

class Player(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(
            stretch_wid=1,
            stretch_len=5
        )
        self.color("white")
        self.speed("fastest")
        self.goto(pos)

    def move_left(self):
        if self.xcor() != -500:
            new_x = self.xcor() - 20
            self.goto(x=new_x,y=-200)

    def move_right(self):
        # print(self.ycor())
        if self.xcor() != 500:
            new_x = self.xcor() + 20
            self.goto(x=new_x,y=-200)

    def shoot(self, aliens):
        bullet = Bullet()
        bullet.goto(y=self.ycor(),x=self.xcor())
        bullet.move_bullet()
        for alien in aliens:
            if bullet.ycor() and bullet.xcor() == alien:
                alien.goto(y=3000, x=3000)


