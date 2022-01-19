from tkinter import *
import math

wn = Tk()
wn.geometry("312x324")
wn.resizable(0,0)
wn.title("Calculator")

#Function
def btn_click(num):
    global expression
    expression += num
    text_polish.set(expression)
    

def btn_clear():
    global expression
    expression = ""
    text_polish.set("")

def bton_equal():
    global expression
    
    expression = str(eval(expression))
    if expression[-1] == "0" and expression[-2] == ".":
        expression = str(int(eval(expression)))
    text_polish.set(expression)
    expression = ""

def bton_del():
    global expression
    expression = expression[:-1]
    text_polish.set(expression)

#input field

expression = ""

text_polish = StringVar()

text_frame = Frame(wn, width=312, height=50, bd=0, highlightcolor="dark gray", highlightbackground="light blue", highlightthickness=2, bg="#828282")
text_frame.pack(side=TOP)

text_input = Entry(text_frame, font=('arial', 18, 'bold'), textvariable=text_polish, width=50, bg="#828282", bd=0, justify=RIGHT)
text_input.grid(row=0,column=0)
text_input.pack(ipady=10)

#button field
button_frame = Frame(wn, width=312, height=273, bd=0, bg="light blue")
button_frame.pack()

# first row
clear = Button(button_frame, width=32, height=3, text="C", bg="white", fg="black", cursor= "hand2",bd=0, command= lambda: btn_clear())
clear.grid(row=0,columnspan=3, padx=2, pady=2)
btn_div= Button(button_frame, width=10, height=3, text="/", bg="white", fg="black", command=lambda : btn_click("/"), bd=0)
btn_div.grid(row=0,column=3, padx=1, pady=1)

# second row
btn_1 = Button(button_frame, width=10, height=3, text="1", bg="white", fg="black", command= lambda: btn_click("1"), bd=0)
btn_1.grid(row=1,column=0, padx=1, pady=1)
btn_2 = Button(button_frame, width=10, height=3, text="2", bg="white", fg="black", command= lambda: btn_click("2"), bd=0)
btn_2.grid(row=1,column=1, padx=1, pady=1)
btn_3 = Button(button_frame, width=10, height=3, text="3", bg="white", fg="black", command= lambda: btn_click("3"), bd=0)
btn_3.grid(row=1,column=2, padx=1, pady=1)
btn_multi = Button(button_frame, width=10, height=3, text="*", bg="white", fg="black", command= lambda: btn_click("*"), bd=0)
btn_multi.grid(row=1,column=3, padx=1, pady=1)

# third row
btn_4 = Button(button_frame, width=10, height=3, text="4", bg="white", fg="black", command= lambda: btn_click("4"), bd=0)
btn_4.grid(row=2,column=0, padx=1, pady=1)
btn_5 = Button(button_frame, width=10, height=3, text="5", bg="white", fg="black", command= lambda: btn_click("5"), bd=0)
btn_5.grid(row=2,column=1, padx=1, pady=1)
btn_6 = Button(button_frame, width=10, height=3, text="6", bg="white", fg="black", command= lambda: btn_click("6"), bd=0)
btn_6.grid(row=2,column=2, padx=1, pady=1)
btn_plus = Button(button_frame, width=10, height=3, text="+", bg="white", fg="black", command= lambda: btn_click("+"), bd=0)
btn_plus.grid(row=2,column=3, padx=1, pady=1)

# fourth row
btn_7 = Button(button_frame, width=10, height=3, text="7", bg="white", fg="black", command= lambda: btn_click("7"), bd=0)
btn_7.grid(row=2,column=0, padx=1, pady=1)
btn_8 = Button(button_frame, width=10, height=3, text="8", bg="white", fg="black", command= lambda: btn_click("8"), bd=0)
btn_8.grid(row=2,column=1, padx=1, pady=1)
btn_9 = Button(button_frame, width=10, height=3, text="9", bg="white", fg="black", command= lambda: btn_click("9"), bd=0)
btn_9.grid(row=2,column=2, padx=1, pady=1)
btn_minus = Button(button_frame, width=10, height=3, text="-", bg="white", fg="black", command= lambda: btn_click("-"), bd=0)
btn_minus.grid(row=2,column=3, padx=1, pady=1)

# fifth row
btn_dot = Button(button_frame, width=10, height=3, text=".", bg="white", fg="black", command= lambda: btn_click("."), bd=0)
btn_dot.grid(row=3,column=0, padx=1, pady=1)
btn_0 = Button(button_frame, width=10, height=3, text="0", bg="white", fg="black", command= lambda: btn_click("0"), bd=0)
btn_0.grid(row=3,column=1, padx=1, pady=1)
btn_equal = Button(button_frame, width=21, height=3, text="=", bg="white", fg="black", command= lambda: bton_equal(), bd=0)
btn_equal.grid(row=3,column=2, padx=1, pady=1, columnspan=2)

# sixth row
btn_del = Button(button_frame, width=43, height=3, text="DEL", bg="white", fg="black", command= lambda : bton_del(), bd=0)
btn_del.grid(row=4,column=0, padx=1, pady=1, columnspan=4)
wn.mainloop()