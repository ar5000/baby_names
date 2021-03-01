from tkinter import *
from PIL import ImageTk, Image

def box_check_status():
    global my_label
    # if 'my_label' in globals():
    #     my_label.grid_forget()

    my_label = Label(root, text=var.get()).pack()

def main():
    global root, check1, var
    root = Tk()

    root.title("w_Coding Homework")
    root.iconbitmap('tkinter/images/baby.ico')
    root.geometry("400x400")

    var = StringVar(value='On')

    check1 = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off", command=box_check_status)
    check1.deselect()
    check1.pack()

    myLabel = Label(root, text="var.get()").pack()

    btn = Button(root, text='show check status', command=box_check_status).pack()

    root.mainloop()

if __name__ == '__main__':
    main()