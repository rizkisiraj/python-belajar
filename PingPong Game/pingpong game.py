import turtle
import time

paused = False
pausing = turtle.Turtle()
pausing.hideturtle()


#setting screen
wn = turtle.Screen()
wn.setup(width=800,height=600)
wn.bgcolor("black")
# wn.bgpic("PingPong Game\lostari.gif") uncomment biar make foto rian
wn.tracer(0)

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
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball_dx = 9
ball_dy = 9

# setting score
score = turtle.Turtle()
score1 = 0
score2 = 0
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Player 1: {score1}          Player 2: {score2}", align="center", font=("Game Over", 32, "normal"))

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

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
        

#listen keyboard
wn.listen()
wn.onkeypress(leftpad_up,"w")
wn.onkeypress(leftpad_down,"s")
wn.onkeypress(rightpad_up,"Up")
wn.onkeypress(rightpad_down,"Down")
wn.onkeypress(toggle_pause,"p")

while True:
    time.sleep(0.02)
    if is_paused:
        pausing.speed(0)
        pausing.color("white")
        pausing.penup()
        pausing.goto(0,0)
        pausing.write("PAUSE", align="center", font=("Game Over", 32, "normal"))
        ball.setx(ball.xcor())
        ball.sety(ball.ycor())
        wn.update()
    else:

        pausing.clear()
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
            score1 += 1
            score.write(f"Player 1: {score1}          Player 2: {score2}", align="center", font=("Game Over", 32, "normal"))
            ball_dy *= -1

        if ball.xcor() < -400:
            ball.goto(0,0)
            score2 += 1
            score.clear()
            score.write(f"Player 1: {score1}          Player 2: {score2}", align="center", font=("Game Over", 32, "normal"))
            ball_dy *= -1

        #collisions
        if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < rightpad.ycor() + 60) and (ball.ycor() > rightpad.ycor() - 60):
            ball.setx(350)
            ball_dx *= -1

        if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < leftpad.ycor() + 60) and (ball.ycor() > leftpad.ycor() - 60):
            ball.setx(-350)
            ball_dx *= -1

        if score2 == 10 or score1 == 10:
            break

turtle.mainloop()