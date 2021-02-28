from tkinter import *

root = Tk()

def my_click():
    my_label = Label(root, text= "Look!  I clicked on a button!")
    my_label.grid(column=0, row=2)


my_button = Button(root, text="Click Me!", state = "normal", padx=50, command=my_click)
my_button.grid(row= 0, column= 0)


root.mainloop()