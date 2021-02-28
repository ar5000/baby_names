from tkinter import *
from types import LambdaType
from PIL import ImageTk, Image
from tkinter import messagebox

def main():

    root = Tk()
    root.title('Learn to Code at w_coding')
    root.iconbitmap('tkinter/images/baby.ico')

    #showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    def popup():
        response = messagebox.askyesno("Popup Title", "Hellow WOrld")
        Label(root, text=response).pack()
        if response:
            Label(root, text="Clicked Yes").pack()
        if not response:
            Label(root, text="Clicked No").pack()

    Button(root, text="Popup", command=popup).pack()

    
    root.mainloop()

if __name__ == '__main__':
    main()