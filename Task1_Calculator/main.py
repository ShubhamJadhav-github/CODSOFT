# CODSOFT Internship
# Task
# Shubham Ashok Jadhav

from tkinter import *
from tkinter import messagebox

win = Tk()
# Configure title of window
win.title("Calculator")
# Configure widow height, width and horizontal, vertical position
win.geometry("650x300+250+100")
# Disable the resizing of window by height and width
win.resizable(False, False)
LabelFont1 = ('times new roman', 20, 'bold')
LabelFont2 = ('courier', 15)

# For Command = Add in button b1
def add():
    try:
        a = float(e1.get())
        b = float(e2.get())
        a += b
        l4.config(text='x + y =')
        l5.config(text=a)
    except ValueError:
        messagebox.showerror("Value Error","Only Numbers are allowed")

# For Command = sub in button b2
def sub():
    try:
        a = float(e1.get())
        b = float(e2.get())
        a -= b
        l4.config(text='x - y =')
        l5.config(text=a)
    except ValueError:
        messagebox.showerror("Value Error","Only Numbers are allowed")

# For Command = mul in button b3
def mul():
    try:
        a = float(e1.get())
        b = float(e2.get())
        a *= b
        l4.config(text='x * y =')
        l5.config(text=a)
    except ValueError:
        messagebox.showerror("Value Error","Only Numbers are allowed")

# For Command = div in button b4
def div():
    try:
        a = float(e1.get())
        b = float(e2.get())
        a /= b
        l4.config(text='x / y =')
        l5.config(text=a)
    except ValueError:
        messagebox.showerror("Value Error","Only Numbers are allowed")

# Main Title Labael
l1 = Label(win, text='Calculator', font=LabelFont1)
l1.place(x=250, y=10)
# First Value Label
l2 = Label(win, text='Enter value for x', font=LabelFont2)
l2.place(x=50, y=50)
# First Value Entry
e1 = Entry(win, font=LabelFont2)
e1.place(x=300, y=50)
# Second Value Label
l3 = Label(win, text='Enter value for y', font=LabelFont2)
l3.place(x=50, y=100)
# Second Value Entry
e2 = Entry(win, font=LabelFont2)
e2.place(x=300, y=100)
# Result label which will show x + y or x - y or x * y or x / y
l4 = Label(win, text='----', font=LabelFont2)
l4.place(x=50, y=150)
# Result label which will show actual result
l5 = Label(win, text='----', font=LabelFont2)
l5.place(x=300, y=150)
# Addition command button
b1 = Button(win, text="Add", font=LabelFont2, command=add)
b1.place(x=150, y=200)
# Subtraction command button
b2 = Button(win, text="Sub", font=LabelFont2, command=sub)
b2.place(x=250, y=200)
# Multiplication command button
b3 = Button(win, text="Mul", font=LabelFont2, command=mul)
b3.place(x=350, y=200)
# Division Command Button
b4 = Button(win, text="Div", font=LabelFont2, command=div)
b4.place(x=450, y=200)

win.mainloop()
