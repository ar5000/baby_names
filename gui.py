import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, Menu


import baby_names

# ----------------------------
# GUI Setup
# ---------------------------
window = tk.Tk()

window.title('Baby Names')
window.resizable(True,True)



# ------------------------------
# Callbacks
# ----------------------------

def press_me_action():
    # click_action.configure(text='You clicked me!')
    # welcome_label.configure(foreground='Blue')
    # click_action.configure(text='Now this is blue')
    welcome_label.configure(text=f'Looking up for ...{baby_name.get()}')

def gracefully_exit():
    window.quit()
    window.destroy()
    exit()

main_cont = ttk.LabelFrame(window, text="Options")
main_cont.grid(column=0, row=0, padx=20, pady=20)


# ----------------------------
# Widgets
# ----------------------------

welcome_label = ttk.Label(main_cont, text="Welcome to the Baby Names extractor")
welcome_label.grid(column=0, row=0)

click_action = ttk.Button(main_cont, text="Press Me!!", command=press_me_action)
click_action.grid(column=0, row=2)

baby_name = tk.StringVar()
text_box_name = ttk.Entry(main_cont, width=20, textvariable=baby_name)
text_box_name.grid(column=0, row=1)

choose_file_label = ttk.Label(main_cont, text="Choose a file to extract baby data")
choose_file_label.grid(column=2, row= 0)
# file_chosen_cb = ttk.Combobox(main_cont, width = 15, textvariable=file_s)

file_chosen = tk. StringVar()
file_chosen_cb = ttk.Combobox(main_cont, width=20, textvariable = file_chosen, state='readonly')
file_chosen_cb['values'] = (baby_names.what_files())
file_chosen_cb.grid(column= 0, row = 3)
file_chosen_cb.current(1)

# Check Boxes

rank = tk.IntVar()
male = tk.IntVar()
female = tk.IntVar()

rank_checkbox = ttk.Checkbutton(main_cont, text="Rank", variable=rank)
male_checkbox = ttk.Checkbutton(main_cont, text="Male", variable=male)
female_checkbox = ttk.Checkbutton(main_cont, text="Female", variable=female)
rank_checkbox.grid(column=0, row=4, sticky=tk.W)
male_checkbox.grid(column=1, row=4, sticky=tk.W)
female_checkbox.grid(column=2, row=4, sticky=tk.W)

# Radio Button

data_order = tk.IntVar()
desc_radio = tk.Radiobutton(main_cont, text='Descending', variable=data_order, value=1)
asc_radio = tk.Radiobutton(main_cont, text='Ascending', variable=data_order, value=2)

desc_radio.grid(column=0, row=5)
asc_radio.grid(column=1, row=5)

scrollable_text = scrolledtext.ScrolledText(main_cont, width=40, height=3, wrap=tk.WORD)
scrollable_text.grid(column=0, columnspan=3, row=6)

scrollable_text.insert(tk.INSERT, file_chosen_cb.current(1), )
scrollable_text.configure(state="disabled")

btn_frame = ttk.LabelFrame(main_cont, text="This is a label")
btn_frame.grid(column=0,  row=7)

ttk.Label(btn_frame, text="Hello!").grid(column=0, row=0, sticky=tk.W)
ttk.Label(btn_frame, text='Hiiii!').grid(column=0, row=1, sticky=tk.W)
ttk.Label(btn_frame, text='Howdy!').grid(column=0, row=2, sticky=tk.W)

for child in btn_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

# -------------------
# MENU BAR
# -------------------

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=gracefully_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

# -------------------
# UX Modifiers
# -------------------
text_box_name.focus()


# ---------------------------
# START UI
# ---------------------------

window.mainloop()