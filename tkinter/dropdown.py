from tkinter import *
from PIL import ImageTk, Image

def show():
    my_label = Label(root, text=clicked.get()).pack()

def main():
    global root, clicked
    root = Tk()

    root.title("w_Coding Homework")
    root.iconbitmap('tkinter/images/baby.ico')
    root.geometry("400x400")

    clicked = StringVar(value="Monday")

    days_of_the_week = ['Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']

    drop = OptionMenu(root, clicked, *days_of_the_week)
    drop.pack()

    my_button = Button(root, text='Show Selection', command=show).pack()

    root.mainloop()

if __name__ == '__main__':
    main()