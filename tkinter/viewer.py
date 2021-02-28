from tkinter import *
from PIL import ImageTk, Image
from baby_names import what_files


def forward():
    global my_label, image_num, pics, back_button, forward_button
    my_label.grid_forget()
    image_num += 1
    my_label = Label(image=pics[image_num])
    my_label.grid(row=0, column=0, columnspan=3)

    back_button = Button(root, text="<<", command=back, state=ACTIVE, padx=20, pady=10).grid(row=1, column=0)

    if image_num + 1 == len(pics):
        forward_button = Button(root, text=">>", state=DISABLED, padx=20, pady=10).grid(row=1, column=2)

    status = Label(root, text=f"Image {image_num+1} of {len(pics)}", bd=1, relief=SUNKEN, padx=30, pady=10, anchor=E).grid(row=2, column=0, columnspan=3, sticky=W+E)

def back():
    global my_label, image_num, pics, back_button, forward_button
    my_label.grid_forget()
    image_num -= 1
    my_label = Label(image=pics[image_num])
    my_label.grid(row=0, column=0, columnspan=3)
    forward_button = Button(root, text=">>", state=ACTIVE, command=forward, padx=20, pady=10).grid(row=1, column=2)

    if image_num  == 0:
        back_button = Button(root, text="<<", state=DISABLED, padx=20, pady=10).grid(row=1, column=0)
    status = Label(root, text=f"Image {image_num+1} of {len(pics)}", bd=1, relief=SUNKEN, padx=30, pady=10, anchor=E).grid(row=2, column=0, columnspan=3, sticky=W+E)

def main():
    global root, pics, image_num, back_button, forward_button, button_quit, my_label
    root = Tk()
    root.title('Images')
    root.iconbitmap('tkinter/images/baby.ico')

    pics = [ImageTk.PhotoImage(Image.open(pic)) for pic in what_files("tkinter/images")]
    
    image_num = 0

    status = Label(root, text=f"Image {image_num+1} of {len(pics)}", bd=1, relief=SUNKEN, padx=30, pady=10, anchor=E).grid(row=2, column=0, columnspan=3, sticky=W+E)


    my_label = Label(image=pics[0])
    my_label.grid(row=0, column=0, columnspan=3)

    

    back_button = Button(root, text="<<", command= back, state=DISABLED, padx=20, pady=10).grid(row=1, column=0)
    button_quit = Button(root, text="Exit Viewer", command=root.quit, padx=20, pady=10).grid(row=1, column=1)
    forward_button = Button(root, text=">>", command= forward, padx=20, pady=10).grid(row=1, column=2, pady=10)
    

    root.mainloop()


if __name__ == '__main__':
    main()





