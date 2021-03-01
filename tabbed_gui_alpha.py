import tkinter as tk
from tkinter import ttk
import baby_names

window = tk.Tk()

window.title("Baby Names with Tabs")
window.resizable(True,True)

# -------------------
# Tabs
# -------------------

tab_control = ttk.Notebook(window)
tab_one = ttk.Frame(tab_control)
tab_control.add(tab_one, text="Tab #1")

tab_two = ttk.Frame(tab_control)
tab_control.add(tab_two, text="Tab #2")

tab_control.pack(expand=1, fill="both")


# -------------------
# Widgets
# -------------------

tab_frame = ttk.LabelFrame(tab_one, text="This is a label")
tab_one.grid(column=0,  row=7)

ttk.Label(tab_one, text="Hello!").grid(column=0, row=0, sticky=tk.W)

ttk.Label(tab_two, text='Hiiii!').grid(column=0, row=1, sticky=tk.W)


for child in tab_one.winfo_children():
    child.grid_configure(padx=4, pady=2)




window.mainloop()