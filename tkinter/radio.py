from tkinter import *
from types import LambdaType
from PIL import ImageTk, Image

def main():
    global root
    root = Tk()
    root.title('Learn to Code at w_coding')
    root.iconbitmap('tkinter/images/baby.ico')

    # r = IntVar()
    # r.set("2")

    MODES = [
        ("Pepperoni", "Pepperoni"),
        ("Cheese","Cheese"),
        ("Mushroom", "Mushroom"),
        ("Onion", "Onion")
        ]

    pizza = StringVar()
    pizza.set("Pepperoni")

    for text, mode in MODES:
        Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


    def clicked(value):
        global my_label
        # my_label.grid_forget()
        my_label = Label(root, text=value).pack()

    my_button = Button(root, text="Update", command= lambda: clicked(pizza.get()))
    my_button.pack()

    # Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
    # Radiobutton(root, text="Option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack()
    
    # global my_label
    # my_label = Label(root, text=pizza.get()).pack()

    
    root.mainloop()

if __name__ == '__main__':
    main()