import tkinter as tk
from tkinter import ttk

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


# ----------------------------
# Widgets
# ----------------------------

welcome_label = ttk.Label(window, text="Welcome to the Baby Names extractor")
welcome_label.grid(column=0, row=0)

click_action = ttk.Button(window, text="Press Me!!", command=press_me_action)
click_action.grid(column=0, row=2)

baby_name = tk.StringVar()
text_box_name = ttk.Entry(window, width=20, textvariable=baby_name)
text_box_name.grid(column=0, row=1)

choose_file_label = ttk.Label(window, text="Choose a file to extract baby data")
choose_file_label.grid(column=2, row= 0)
# file_chosen_cb = ttk.Combobox(window, width = 15, textvariable=file_s)

file_chosen = tk. StringVar()
file_chosen_cb = ttk.Combobox(window, width=15, textvariable = file_chosen, state='readonly')
file_chosen_cb['values'] = ('baby1990.html','baby1991.html')
file_chosen_cb.grid(column= 0, row = 3)
file_chosen_cb.current(1)

# Check Boxes

rank = tk.IntVar()
male = tk.IntVar()
female = tk.IntVar()

rank_checkbox = ttk.Checkbutton(window, text="Rank", variable=rank)
male_checkbox = ttk.Checkbutton(window, text="Male", variable=male)
female_checkbox = ttk.Checkbutton(window, text="Female", variable=female)
rank_checkbox.grid(column=1, row=4, sticky=tk.W)
male_checkbox.grid(column=2, row=4, sticky=tk.W)
female_checkbox.grid(column=3, row=4, sticky=tk.W)

# Radio Button

data_order = tk.IntVar()
desc_radio = tk.Radiobutton(window, text='Descending', variable=data_order, value=1)
asc_radio = tk.Radiobutton(window, text='Ascending', variable=data_order, value=2)

desc_radio.grid(column=0, row=5)
asc_radio.grid(column=1, row=5)



# -------------------
# UX Modifiers
# -------------------
text_box_name.focus()


# ---------------------------
# START UI
# ---------------------------

window.mainloop()