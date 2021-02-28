from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Images')
root.iconbitmap('baby.ico')


my_image = ImageTk.PhotoImage(Image.open("cave.jpg"))
my_label = Label(image=my_image)
my_label.pack()


button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()



root.mainloop()
