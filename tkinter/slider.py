from tkinter import *
from PIL import ImageTk, Image

def slide(var):
    root.geometry(f'{str(horizontal.get())}x{str(vertical.get())}')


def main():
    global root, horizontal, vertical
    root = Tk()

    root.title("w_Coding Homework")
    root.iconbitmap('tkinter/images/baby.ico')
    root.geometry("400x400")

    vertical = Scale(root, from_=200, to=600, command=slide)
    vertical.grid(row=1, column=0, sticky=N)
    
    horizontal= Scale(root, from_=200, to=600, orient=HORIZONTAL, command=slide)
    horizontal.grid(row=0, column=0, columnspan=2, sticky=W)

    # my_hlabel = Label(root, text=horizontal.get()).grid()
    # my_vlabel = Label(root, text=vertical.get()).grid()

    # my_btn = Button(root, text='update window', command=slide).grid(row=3, column=0)

    root.mainloop()

if __name__ == '__main__':
    main()