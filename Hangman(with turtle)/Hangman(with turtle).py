import turtle
import random

t = turtle.Turtle()

# rules for the game
def da_rules(x):
    if x == 5:
        t.left(90)
        t.fd(50)
        t.right(90)
        t.circle(50)
        t.penup()

    elif x == 4:
        t.goto(-51,49)
        t.pendown()
        t.goto(-51,-151)

    elif x == 3:
        t.left(60)
        t.forward(100)
        t.backward(100)

    elif x == 2:
        t.left(60)
        t.forward(100)
        t.backward(100)

    elif x == 1:
        t.right(30)
        t.goto(-51,49)
        t.forward(20)
        t.right(60)
        t.forward(100)
        t.backward(100)

    elif x == 0:
        t.left(120)
        t.forward(100)
        t.backward(100)

# prepare turtle
t.hideturtle()
turtle.hideturtle()
t.speed(10)
turtle.speed(0)
t.penup()
t.forward(100)
t.right(90)
t.forward(300)
t.right(180)
t.pendown()
t.forward(500)
t.left(90)
t.fd(150)
turtle.penup()
turtle.delay(0)

# hangman gameplay
def hangman():
    wordbank = ['lebron', 'durant', 'curry', 'harris', 'embiid', 'simmons']
    tries = 6
    main_word = 'abcdefghijklmnopqrstuvwxyz'
    word = random.choice(wordbank)
    guessmade = ''
    t.speed(10)
    while len(word) > 0:
        turtle.goto(-135,230)
        main = ''
        for letter in word:
            if letter in guessmade:
                turtle.write(letter + ' ', True, font=("Courier", 14, "normal"))
                main += letter
            else:
                turtle.write('_ ', True, font=("Courier", 14, "normal"))
        
        if main == word:
            break
        
        guess = turtle.textinput("Hangman", "Guess the word: ")
        
        if guess in main_word:
            guessmade += guess
        else:
            guess = turtle.textinput("Hangman","INPUT A VALID WORD ")
        
        if guess not in word:
            tries -= 1
            da_rules(tries)

hangman()