from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=3)
e.grid(row= 0, column=0 )
e.insert(0, "Enter Your Name: ")


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text= hello)
    my_label.grid(column=0, row=2)


my_button = Button(root, text="Enter Your Name", state = "normal", padx=50, command=my_click)
my_button.grid(row= 1, column= 0)


root.mainloop()