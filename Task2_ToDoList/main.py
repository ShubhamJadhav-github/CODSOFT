from tkinter import *
from tkinter.ttk import Combobox
import os

# Get the directory where the Python script is located
current_directory = os.path.dirname(os.path.realpath(__file__))
# Specify the name of the text file you want to create
file_name = "data.txt"
# Combine the directory path and file name to get the full file path
file_path = os.path.join(current_directory, file_name)
global file
global cb
global combolst
global tasks
try:
    file = open(file_path, 'x')
    file.close()
except FileExistsError:
    file = open(file_path, 'r')
    tasks = file.read()
    combolst = list(tasks.split("\n"))
    file.close()

win = Tk()
win.title("To Do List Application")
win.geometry("675x350+270+100")
win.config(bg='#3846c7')
f1 = ('Arial', 40, 'bold')
f2 = ('Arial', 15, 'bold')
f3 = ('Arial', 10)
TextArea = Text(win, width=30, height=20)
TextArea.config(state=NORMAL)
TextArea.delete('1.0', END)
TextArea.insert('1.0', tasks)
TextArea.config(state=DISABLED)


def newentry():
    global file
    global tasks
    if e1.get() == '':
        pass
    else:
        combolst.append(e1.get())
        task = e1.get() + '\n'
        tasks = tasks + task
        file = open(file_path, 'a')
        file.write(task)
        file.close()
        TextArea.config(state=NORMAL)
        TextArea.delete('1.0', END)
        TextArea.insert('1.0', tasks)
        TextArea.config(state=DISABLED)
    e1.delete(0, END)


def removeitem():
    global cb
    global file
    index = cb.current()  # get current index number of combobox selected item
    print(index)
    TextArea.config(state=NORMAL)
    TextArea.delete(END, cb.get())
    TextArea.config(state=DISABLED)


l1 = Label(win, text="To Do List Application", fg='white', bg='#3846c7', font=('Arial', 20, 'bold'))
l1.grid(row=0, column=0)

e1 = Entry(win, font=f2)
e1.grid(row=1, column=0, pady=10)
b1 = Button(win, text="Add task to the list", font=f3, command=newentry)
b1.grid(row=2, column=0)

cb = Combobox(win, values=combolst)
cb.config(font=f2)
cb.grid(row=3, column=0, pady=50, padx=10)
b2 = Button(win, text="Remove Item", font=f3, command=removeitem)
b2.grid(row=3, column=1)

b3 = Button(win, text="Exit", font=f3, command=win.destroy)
b3.grid(row=4, column=0)

TextArea.place(x=400, y=0)
win.mainloop()
file.close()
