import turtle
import time

#setting screen
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.title("flappy bird")
wn.tracer(0)

#setting bird
bird = turtle.Turtle()
bird.shape("square")
bird.color("white")
bird.speed(0)
bird.penup()
bird.goto(0,0)
gravity = -5

#obstacle
obs_one_up = turtle.Turtle()
obs_one_up.shape("square")
obs_one_up.color("green")
obs_one_up.shapesize(stretch_wid=20, stretch_len=5)
obs_one_up.speed(0)
obs_one_up.penup()
obs_one_up.goto(300,300)
obs_one_up_dx = -12

obs_one_down = turtle.Turtle()
obs_one_down.shape("square")
obs_one_down.color("green")
obs_one_down.shapesize(stretch_wid=25, stretch_len=5)
obs_one_down.speed(0)
obs_one_down.penup()
obs_one_down.goto(300,-300)
obs_one_down_dx = -12

#obstacle2
obs_one_up1 = turtle.Turtle()
obs_one_up1.shape("square")
obs_one_up1.color("green")
obs_one_up1.shapesize(stretch_wid=30, stretch_len=5)
obs_one_up1.speed(0)
obs_one_up1.penup()
obs_one_up1.goto(600,300)
obs_one_up1_dx = -12

obs_one_down1 = turtle.Turtle()
obs_one_down1.shape("square")
obs_one_down1.color("green")
obs_one_down1.shapesize(stretch_wid=20, stretch_len=5)
obs_one_down1.speed(0)
obs_one_down1.penup()
obs_one_down1.goto(600,-300)
obs_one_down1_dx = -12

#function
def move_up():
    y = bird.ycor()
    y += 50
    bird.sety(y)

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
#keyboard
wn.listen()
wn.onkeypress(move_up,"Up")
wn.onkeypress(toggle_pause, "p")

#da game
while True:
    time.sleep(0.02)

    wn.update()

    bird.sety(bird.ycor()+gravity)

    obs_one_up.setx(obs_one_up.xcor()+obs_one_up_dx)
    obs_one_down.setx(obs_one_down.xcor()+obs_one_down_dx)
    obs_one_up1.setx(obs_one_up1.xcor()+obs_one_up1_dx)
    obs_one_down1.setx(obs_one_down1.xcor()+obs_one_down1_dx)

    if obs_one_up.xcor() < -400:
        obs_one_up.goto(300,300)
    if obs_one_down.xcor() <-400:
        obs_one_down.goto(300,-300)

    if obs_one_up1.xcor() < -400:
        obs_one_up1.goto(300,300)
    if obs_one_down1.xcor() <-400:
        obs_one_down1.goto(300,-300)

turtle.mainloop()