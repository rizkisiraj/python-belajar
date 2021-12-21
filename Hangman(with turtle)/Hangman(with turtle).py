import turtle
import random

t = turtle.Turtle()
wn = turtle.Screen()
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
        new_game = turtle.textinput("do u want to play again?", "'y' for yes and 'n' for no")
        while bool(new_game) == False:
            new_game = turtle.textinput("input valid key", "'y' for yes and 'n' for no")
            
        if new_game == 'y':
            wn.clear()
            hangman()
        elif new_game == 'n':
            quit()
        

# prepare turtle
def prepare_turtle():
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
    wordbank = ['lebron']
    control_word = 'yn'
    tries = 6
    main_word = 'abcdefghijklmnopqrstuvwxyz'
    word = random.choice(wordbank)
    guessmade = ''
    t.reset()
    turtle.reset()
    prepare_turtle()
    while len(word) > 0:
        turtle.goto(-135,-300)
        main = ''
        for letter in word:
            if letter in guessmade:
                turtle.write(letter + ' ', True, font=("Courier", 14, "normal"))
                main += letter
            else:
                turtle.write('_ ', True, font=("Courier", 14, "normal"))
        
        if main == word:
            new_game = turtle.textinput("Congratulations!! do u want to play again?", "'y' for yes and 'n' for no")
            while bool(new_game) == False or new_game not in control_word:
                new_game = turtle.textinput("input valid key", "'y' for yes and 'n' for no")
            
            if new_game == 'y':
                wn.clear()
                hangman()
            elif new_game == 'n':
                quit()


        

        guess = turtle.textinput("Hangman", "Guess the word: ")
        
        if guess in main_word:
            guessmade += guess
        else:
            guess = turtle.textinput("Hangman","INPUT A VALID WORD ")
        
        if guess not in word:
            tries -= 1
            da_rules(tries)

hangman()
turtle.mainloop()
t.mainloop()