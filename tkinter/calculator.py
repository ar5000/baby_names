from tkinter import *


root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=2)
e.grid(row= 0, column=0, columnspan=4, padx=10, pady=20 )

def button_click(number):
    # e.delete(0, END)
    e.insert(0,number)
    return


def button_clear():
    e.delete(0, END)

def button_equal():
    num2 = e.get()
    e.delete(0,END)
    if num2:
        num2 = int(num2)
        if operator == 'add':
            e.insert(0, num1 + num2)
        if operator == 'subtract':
            e.insert(0, num1 - num2)
        if operator == 'multiply':
            e.insert(0, num1 * num2)
        if operator == 'divide':
            e.insert(0, num1 / num2)

    # num1 = e.get()

def button_add():
    global num1
    global operator
    operator = 'add'
    num1 = e.get()
    e.delete(0, END)
    if num1:
        num1 = int(num1)
    return

def button_subtract():
    global num1
    global operator
    operator = 'subtract'
    num1 = e.get()
    e.delete(0, END)
    if num1:
        num1 = int(num1)
    return

def button_multiply():
    global num1
    global operator
    operator = 'multiply'
    num1 = e.get()
    e.delete(0, END)
    if num1:
        num1 = int(num1)
    return

def button_divide():
    global num1
    global operator
    operator = 'divide'
    num1 = e.get()
    e.delete(0, END)
    if num1:
        num1 = int(num1)
    return


button_1= Button(root, text=1, padx=40, pady=20, command= lambda: button_click(1))
button_2= Button(root, text=2, padx=40, pady=20, command=lambda: button_click(2))
button_3= Button(root, text=3, padx=40, pady=20, command=lambda: button_click(3))
button_4= Button(root, text=4, padx=40, pady=20, command=lambda: button_click(4))
button_5= Button(root, text=5, padx=40, pady=20, command=lambda: button_click(5))
button_6= Button(root, text=6, padx=40, pady=20, command=lambda: button_click(6))
button_7= Button(root, text=7, padx=40, pady=20, command=lambda: button_click(7))
button_8= Button(root, text=8, padx=40, pady=20, command=lambda: button_click(8))
button_9= Button(root, text=9, padx=40, pady=20, command=lambda: button_click(9))
button_0= Button(root, text=0, padx=40, pady=20, command=lambda: button_click(0))

button_add= Button(root, text='+', padx=39, pady=20, command=button_add)
button_subtract= Button(root, text='-', padx=39, pady=20, command=button_subtract)
button_multiply= Button(root, text='*', padx=39, pady=20, command=button_multiply)
button_divide= Button(root, text='/', padx=39, pady=20, command=button_divide)
button_equal= Button(root, text='=', padx=40, pady=20, command=button_equal)
button_clear= Button(root, text='Clear', padx=30, pady=20, command=button_clear)

# Put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1,column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=1)



root.mainloop()