from tkinter import *
from types import LambdaType
from PIL import ImageTk, Image
from tkinter import messagebox

def open():

    top = Toplevel()
    # lbl = Label(top, text='Hello World').pack()
    my_img = ImageTk.PhotoImage(Image.open("tkinter/images/cave.jpg"))
    


def main():

    root = Tk()
    root.title('Learn to Code at w_coding')
    root.iconbitmap('tkinter/images/baby.ico')

    my_label = Label(top, image=my_img).pack()



    root.mainloop()

if __name__ == '__main__':
    main()