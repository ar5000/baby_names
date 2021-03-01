from tkinter import *
from tkinter import ttk
from tkinter import filedialog, scrolledtext
import os
import baby_names



def file_chooser():
    global window, files_chosen, names
    window.filename = filedialog.askopenfilenames(initialdir=os.getcwd(), title='Select Files to Parse', filetypes=(("HTML",".html"),("All Files","*.*")))
    file_name_labels = [Label(file_parser_frame_left, text=name) for name in window.filename]

    for num, file in enumerate(file_name_labels):
        file.grid(row=num+2, column = 0)
 
    for file in window.filename:
        names.update(baby_names.baby_names_parser(file))

    # year_selection = IntVar()

    # [Radiobutton(file_parser_frame_left, text=year, variable=year_selection, value=years).grid(sticky=N) for year,year, in years]

    scrollable_text = scrolledtext.ScrolledText(file_parser_frame_right, width=40, height=45)
    scrollable_text.grid(column=7, columnspan=5, row=0, sticky=E)

    scrollable_text.insert(INSERT, "".join([f'Name: {name[0]} \t Rank: {name[1]}\n' for name in baby_names.output_names(names, order='rank')]))
    scrollable_text.configure(state="disabled")
    populate_year_checks()
    
def update_text(year_choice, order_selection, gender_selection, start_selection, stop_selection):
    global scrollable_text
    scrollable_text = scrolledtext.ScrolledText(file_parser_frame_right, width=40, height=45)
    scrollable_text.grid(column=7, columnspan=5, row=0, sticky=E)

    scrollable_text.insert(INSERT, [f'Name: {name[0]} \t Rank: {name[1]}\n' for name in baby_names.output_names(names, years=year_choice, order=order_selection, gender=gender_selection, start=start_selection, stop=stop_selection)])
    scrollable_text.configure(state="disabled") 


def populate_year_checks():
    check_box_frame = LabelFrame(file_parser_frame_left, padx=5, pady=5)
    check_box_frame.grid(row=3, column=0, sticky=S)

    years_var_list = [StringVar(value=1) for year in names.keys()]
    years_check_boxes = [Checkbutton(check_box_frame, text=year, variable=year_var, command=update_text) for year, year_var in zip(names.keys(),years_var_list)]

    for check_box in years_check_boxes:
        check_box.pack()

def main():
    global window, my_notebook, my_frame, file_parser, clipboard_parser, regex_parser, names, file_parser_frame_left, file_parser_frame_right
    window = Tk()
    names = {}

    window.title("w_Coding Homework")
    window.iconbitmap('tkinter/images/baby.ico')
    window.geometry("800x800")

    my_notebook = ttk.Notebook(window)

    my_notebook.pack(pady=1)

    file_parser = Frame(my_notebook, width = 800, height=800)
    clipboard_parser = Frame(my_notebook, width=800, height=800)
    regex_parser = Frame(my_notebook, width=800, height=800)

    file_parser.pack(fill='both', expand=1)
    clipboard_parser.pack(fill='both', expand=1)
    regex_parser.pack(fill='both', expand=1)
    
    my_notebook.add(file_parser, text="File Parser")
    my_notebook.add(clipboard_parser, text="Clipboard Parser")
    my_notebook.add(regex_parser, text="Regex Explorer")

    file_parser_frame_left = LabelFrame(file_parser, height=700, padx=5, pady=5)
    file_parser_frame_left.grid(row=0, column=0, sticky=N+W, )
    file_parser_frame_right = LabelFrame(file_parser, padx=5, pady=5)
    file_parser_frame_right.grid( row=0, column=5, stick=N+E)


    open_files = Button(file_parser_frame_left, text="Select Files", command=file_chooser, padx=10, pady=5)
    open_files.grid(padx=10, pady=10, sticky=N+W, row=0, column=0)






    window.mainloop()

if __name__ == '__main__':
    main()