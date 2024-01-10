import time
from turtle import Screen, Turtle
from player import Player
from alien import Alien
from bullet import Bullet
import threading


def move_alien():
    blocks_left_side = False
    blocks_right_side = True
    while blocks_right_side:
        screen.update()
        for block in blocks:
            block.move_left()
        time.sleep(0.1)
        for block in blocks:
            if block.xcor() == -500:
                blocks_left_side = True
                blocks_right_side = False
    while blocks_left_side:
        screen.update()
        for block in blocks:
            block.move_right()
        time.sleep(0.1)
        for block in blocks:
            if block.xcor() == 500:
                blocks_left_side = False
                blocks_right_side = True
    time.sleep(0.1)


def user_alert(message):
    ALIGNMENT = "center"
    FONT = ("times new roman", 24, "normal")
    alert = Turtle()
    alert.hideturtle()
    alert.color("white")
    alert.write(message, align=ALIGNMENT, font=FONT)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")

screen.tracer(0)

player = Player((0, -200))
blocks = []

block01 = Alien((-200,200), "green")
block02 = Alien((-100,200), "green")
block03 = Alien((0,200), "green")
block04 = Alien((100,200),"green")
block05 = Alien((200,200),"green")


block21 = Alien((-200,160), "green")
block22 = Alien((-100,160),"green")
block23 = Alien((0,160),"green")
block24 = Alien((100,160),"green")
block25 = Alien((200,160),"green")


block41 = Alien((-200,120), "green")
block42 = Alien((-100,120), "green")
block43 = Alien((0,120), "green")
block44 = Alien((100,120), "green")
block45 = Alien((200,120),"green")


blocks.append(block01)
blocks.append(block02)
blocks.append(block03)
blocks.append(block04)
blocks.append(block05)


blocks.append(block21)
blocks.append(block22)
blocks.append(block23)
blocks.append(block24)
blocks.append(block25)


blocks.append(block41)
blocks.append(block42)
blocks.append(block43)
blocks.append(block44)
blocks.append(block45)

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player.shoot, 'space')


playing = True
while playing:
    aliens = threading.Thread(move_alien())
    aliens.start()
    time.sleep(0.01)
    screen.update()


screen.update()
screen.exitonclick()
