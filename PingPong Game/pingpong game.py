import turtle
import time
import pygame
from pygame import mixer

#setting screen
wn = turtle.Screen()
wn.setup(width=800,height=600)
wn.bgcolor("black")
# wn.bgpic("PingPong Game\lostari.gif") uncomment biar make foto rian
wn.tracer(0)


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
ball_sound = mixer.Sound("PingPong Game\sfx_coin_cluster7.wav")
paddle_sound = mixer.Sound("PingPong Game\sfx_sounds_button6.wav")

paused = False
pausing = turtle.Turtle()
pausing.hideturtle()

#setting input
player1 = turtle.textinput("player 1", "type your name")
player2 = turtle.textinput("player 2", "type your name")
ballcolor = turtle.textinput("ball color", "insert a color name")
color1 = turtle.textinput("right paddle", "insert a color name")
color2 = turtle.textinput("leftpaddle", "insert a color name")

#setting leftpaddle
rightpad = turtle.Turtle()
rightpad.speed(0)
rightpad.shape("square")
rightpad.color(color1)
rightpad.shapesize(stretch_wid=5, stretch_len=1)
rightpad.penup()
rightpad.goto(360,0)

# setting rightpad
leftpad = turtle.Turtle()
leftpad.speed(0)
leftpad.shape("square")
leftpad.color(color2)
leftpad.shapesize(stretch_wid=5, stretch_len=1)
leftpad.penup()
leftpad.goto(-360,0)

# setting ball
ball = turtle.Turtle()
ball.speed(0)
ball.color(ballcolor)
ball.shape("circle")
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
score.write(f"{player1}: {score1}          {player2}: {score2}", align="center", font=("Game Over", 32, "normal"))

#key function
is_paused = False

def leftpad_up():
    if is_paused == False:
        y = leftpad.ycor()
        y += 50
        y = leftpad.sety(y)

def leftpad_down():
    if is_paused == False:
        y = leftpad.ycor()
        y -= 50
        y = leftpad.sety(y)

def rightpad_up():
    if is_paused == False:    
        y = rightpad.ycor()
        y += 50
        y = rightpad.sety(y)

def rightpad_down():
    if is_paused == False:    
        y = rightpad.ycor()
        y -= 50
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
            ball_sound.play()
            ball.goto(0,0)
            score.clear()
            score1 += 1
            score.write(f"{player1}: {score1}          {player2}: {score2}", align="center", font=("Game Over", 32, "normal"))
            ball_dy *= -1

        if ball.xcor() < -400:
            ball_sound.play()
            ball.goto(0,0)
            score2 += 1
            score.clear()
            score.write(f"{player1}: {score1}          {player2}: {score2}", align="center", font=("Game Over", 32, "normal"))
            ball_dy *= -1

        #collisions
        if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < rightpad.ycor() + 60) and (ball.ycor() > rightpad.ycor() - 60):
            paddle_sound.play()
            ball.setx(350)
            ball_dx *= -1

        if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < leftpad.ycor() + 60) and (ball.ycor() > leftpad.ycor() - 60):
            paddle_sound.play()
            ball.setx(-350)
            ball_dx *= -1

        if score2 == 10 or score1 == 10:
            pausing.speed(0)
            pausing.color("white")
            pausing.penup()
            pausing.goto(0,0)
            if score2 == 10:
                pausing.write("CONGRATURALIONS PLAYER 2 WIN", align="center", font=("Game Over", 32, "normal"))
            else:
                pausing.write("CONGRATURALIONS PLAYER 1 WIN", align="center", font=("Game Over", 32, "normal"))
            break

turtle.mainloop()