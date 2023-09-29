# Task 3 - Password Generator
# Shubham Ashok Jadhav

from tkinter import *
import random
from tkinter.ttk import Combobox
from tkinter import messagebox

win = Tk()
win.title("Password Generator")
win.geometry("600x300+250+50")
win.resizable(False, False)

global password


def generate():
    global password
    password = ''
    try:
        length = int(e1.get())
        difficulty = c1.current()
        if length <= 5 or length > 20:
            print(difficulty)
            messagebox.showinfo("Invalid Length", "Please provide length in between 6 to 20")
            return
        else:
            if difficulty == -1:
                messagebox.showinfo("Invalid difficulty", "Please provide difficulty of password")
                return
            if difficulty == 0:  # Easy
                while length > 0:
                    password += str(random.randint(0, 9))
                    length -= 1
                l4.config(text=password)
            elif difficulty == 1:  # Medium
                alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                while length > 0:
                    switch2 = random.randint(1, 2)
                    if switch2 == 1:
                        password += str(random.randint(0, 9))
                    elif switch2 == 2:
                        password += random.choice(alpha)
                    length -= 1
                l4.config(text=password)
            elif difficulty == 2:  # Difficult
                alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                symbols = "!@#$%^&*()-+;:'\|,<.>/?`~"
                while length > 0:
                    switch3 = random.randint(1, 3)
                    if switch3 == 1:
                        password += str(random.randint(0, 9))
                    elif switch3 == 2:
                        password += random.choice(alpha)
                    elif switch3 == 3:
                        password += random.choice(symbols)
                    length -= 1
                l4.config(text=password)
    except ValueError:
        messagebox.showinfo("Invalid Length", "Please provide valid value")


f1 = ("arial", 15, 'bold')
f2 = ('calibre', 15)

l1 = Label(win, text="Enter length of password(6-20)", font=f1)
l1.place(x=10, y=30)
e1 = Entry(win, font=f2)
e1.place(x=320, y=30)

l2 = Label(win, text="Set Password Complexity", font=f1)
l2.place(x=10, y=90)
data = ['Easy (Only Int)', 'Medium (Int + Alphabets)', 'Hard (Int + Alphabets + Symbols)']
c1 = Combobox(values=data)
c1.config(width=30, justify='center')
c1.place(x=320, y=95)

b1 = Button(win, text="Generate", font=f1, command=generate)
b1.place(x=250, y=150)

l3 = Label(win, text="Password", font=f1)
l3.place(x=200, y=220)

l4 = Label(win, text="- - - - -", font=f1)
l4.place(x=320, y=220)

win.mainloop()
