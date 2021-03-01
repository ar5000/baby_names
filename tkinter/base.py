from tkinter import *
from PIL import ImageTk, Image


def open():
    global my_img
    top = Toplevel()
    top.title("My second window")
    my_img = ImageTk.PhotoImage(Image.open("tkinter/images/cave.jpg"))   
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close Window', command=top.destroy).pack()

def main():

    root = Tk()
    root.title('Learn to Code at w_coding')
    root.iconbitmap('tkinter/images/baby.ico')

    btn = Button(root, text="Open Second Window", command=open).pack()




    root.mainloop()

if __name__ == '__main__':
    main()