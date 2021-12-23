import turtle


#Penyiapan turtle
wn = turtle.Screen()
wn.screensize(600,600)
t = turtle.Turtle()
t.hideturtle()
t.penup()
turtle.delay(0)
t.goto(-300,200)
t.write("Star Wars is a (adjective) (noun) of (adjective)\n versus evil in a (noun) far far away\n There are (adjective) battles between\n (adjective) (noun) in (adjective)\n Space and (adjective) duels in (plural noun)", True, font=('Courier', 14, 'normal'))

word1 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word2 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word3 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word4 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word5 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word6 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word7 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word8 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word9 = turtle.textinput("Madlibs", "Insert a word that is suitable")
word10 = turtle.textinput("Madlibs", "Insert a word that is suitable")

t.clear()
t.goto(-300,200)
t.write(f"Star Wars is a {word1} {word2} of {word3}\n versus evil in a {word4} far far away\n There are {word5} battles between\n {word6} {word7} in {word8}\n Space and {word9} duels in {word10}", True, font=('Courier', 14, 'normal'))

turtle.mainloop()