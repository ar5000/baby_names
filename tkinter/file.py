from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os


def select_files():
    global my_label, my_image, my_image_label
      
    
    root.filename = filedialog.askopenfilename(initialdir=f'os.getcwd', title="Select a file to parse", filetypes=(("HTML",".html"),("All Files","*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


def main():
    global root
    root = Tk()

    root.title("w_Coding Homework")
    root.iconbitmap('tkinter/images/baby.ico')

    btn = Button(root, text="Choose your files", command=select_files)
    btn.pack()
    

    root.mainloop()

if __name__ == '__main__':
    main()