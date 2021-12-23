import turtle
import time

#setting screen
wn = turtle.Screen()
wn.setup(width=800,height=600)
wn.bgcolor("black")

#setting leftpaddle
rightpad = turtle.Turtle()
rightpad.speed(0)
rightpad.shape("square")
rightpad.color("green")
rightpad.shapesize(stretch_wid=5, stretch_len=1)
rightpad.penup()
rightpad.goto(360,0)

# setting rightpad
leftpad = turtle.Turtle()
leftpad.speed(0)
leftpad.shape("square")
leftpad.color("green")
leftpad.shapesize(stretch_wid=5, stretch_len=1)
leftpad.penup()
leftpad.goto(-360,0)

# setting ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0,0)
ball_dx = 8
ball_dy = 8

# setting score
score = turtle.Turtle()
score1 = 0
score2 = 0
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Player 1: {score1}          Player 2: {score2}", align="center", font=("Courier", 14, "normal"))

#key function
def leftpad_up():
    y = leftpad.ycor()
    y += 40
    y = leftpad.sety(y)

def leftpad_down():
    y = leftpad.ycor()
    y -= 40
    y = leftpad.sety(y)

def rightpad_up():
    y = rightpad.ycor()
    y += 40
    y = rightpad.sety(y)

def rightpad_down():
    y = rightpad.ycor()
    y -= 40
    y = rightpad.sety(y)

#listen keyboard
wn.listen()
wn.onkeypress(leftpad_up,"w")
wn.onkeypress(leftpad_down,"s")
wn.onkeypress(rightpad_up,"Up")
wn.onkeypress(rightpad_down,"Down")

while True:
    wn.update()
    

    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1

    if ball.xcor() > 400:
        ball.goto(0,0)
        score.clear()
        score2 += 1
        score.write(f"Player 1: {score1}          Player 2: {score2}", align="center", font=("Courier", 14, "normal"))
        ball_dy *= -1

    if ball.xcor() < -400:
        ball.goto(0,0)
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1}          Player 2: {score2}", align="center", font=("Courier", 14, "normal"))
        ball_dy *= -1

    #collisions
    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < rightpad.ycor() + 60) and (ball.ycor() > rightpad.ycor() - 60):
        ball.setx(350)
        ball_dx *= -1

    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < leftpad.ycor() + 60) and (ball.ycor() > leftpad.ycor() - 60):
        ball.setx(-350)
        ball_dx *= -1

    

turtle.mainloop()