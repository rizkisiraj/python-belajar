import turtle
t = turtle.Turtle()

# setting layar
l = turtle.Screen()
l.bgcolor("salmon")

def curveleft():
    for i in range(180):
        t.left(1)
        t.forward(1)

def curveright():
    for i in range(180):
        t.right(1)
        t.forward(1)

# setting turtle
t.fillcolor("white")
t.shape("circle")
# setting pen
t.pensize(8)

# membuat nama
t.penup()
t.left(90)
t.fd(100)
t.left(90)
t.fd(370)

t.pencolor("red")
t.pendown()
t.fd(30)
curveleft()
curveright()
t.fd(50)

t.penup()
t.fillcolor("red")
t.pencolor("white")
t.shape("arrow")
t.right(180)
t.fd(150)
t.pendown()
t.left(90)
t.fd(230)

t.penup()
t.right(90)
t.fd(50)

t.pencolor("red")
t.fillcolor("white")
t.shape("circle")
t.pendown()
t.fd(50)
curveright()
t.fd(50)
t.right(90)
t.fd(115)
t.backward(115)
t.penup()
t.right(130)
t.pendown()
t.fd(160)
t.backward(160)
t.right(50)
t.fd(115)

t.penup()
t.left(90)
t.fd(170)

t.pencolor("white")
t.fillcolor("red")
t.shape("arrow")
t.pendown()
t.left(60)
t.fd(250)
t.right(120)
t.fd(125)
t.right(120)
t.fd(120)
t.backward(120)
t.left(120)
t.fd(125)

t.penup()
t.left(60)
t.fd(60)

t.pencolor("red")
t.fillcolor("white")
t.shape("circle")
t.pendown()
t.left(90)
for i in range(180):
    t.left(1)
    t.backward(1)
t.backward(230)
turtle.mainloop()