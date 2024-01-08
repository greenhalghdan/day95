import time
from turtle import Screen, Turtle
from player import Player
from alien import Alien
from bullet import Bullet

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

paddle = Player((0, -200))
blocks = []
block01 = Alien((-200,200), "red")
block03 = Alien((100,200),"red")
block05 = Alien((200,200),"red")

block11 = Alien((-200,180), "orange")
block13 = Alien((200,180),"orange")
block15 = Alien((-100,180),"orange")

block21 = Alien((-200,160), "yellow")
block23 = Alien((200,160),"yellow")
block25 = Alien((100,160),"yellow")

block31 = Alien((-200,140), "green")
block33 = Alien((200,140),"green")
block35 = Alien((100,140), "green")

block41 = Alien((-200,120), "blue")
block43 = Alien((200,120),"blue")
block45 = Alien((-100,120), "blue")

blocks.append(block01)
blocks.append(block03)
blocks.append(block05)

blocks.append(block11)
blocks.append(block13)
blocks.append(block15)

blocks.append(block21)
blocks.append(block23)
blocks.append(block25)

blocks.append(block31)
blocks.append(block33)
blocks.append(block35)

blocks.append(block41)
blocks.append(block43)
blocks.append(block45)

bullet = Bullet()
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player.shoot, 'space')


playing = True

while playing:
    time.sleep(0.01)
    screen.update()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()
    if ball.xcor() > 220 or ball.xcor() < -220:
        ball.bounce_x()
    for block in blocks:
        w = int(ball.ycor())
        x = int(ball.xcor())
        y = int(block.xcor())
        z = int(block.ycor())
        if w > z - 20 and w < z + 20 and x > y - 50 and x < y + 50:
            ball.bounce_y()
            block.goto(30000, 3000)
            blocks.remove(block)
            block._hidden_from_screen = True
    if ball.distance(paddle) < 50:
        ball.bounce_y()
    if len(blocks) <= 0:
        user_alert(message="You Win")
        playing = False
    if int(ball.ycor()) < -249:
        user_alert(message="You Lose")
        playing = False

screen.update()
screen.exitonclick()
