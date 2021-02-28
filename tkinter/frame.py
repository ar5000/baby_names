from tkinter import *
from PIL import ImageTk, Image

def main():
    root = Tk()
    root.title('Learn to Code at w_coding')
    root.iconbitmap('tkinter/images/baby.ico')

    frame = LabelFrame(root, padx=50, pady=50)
    frame.pack(padx=5, pady=5)
    
    b = Button(frame, text="don't click here", padx=5, pady=5)
    b2 = Button(frame, text='or here!!')
    b.grid(row=0, pady=0)
    b2.grid(row=1, column=1)
    
    
    
    
    
    root.mainloop()

if __name__ == '__main__':
    main()