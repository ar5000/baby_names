import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread
from time import sleep


class GUI():

    def __init__(self):

        # -------------------------
        # MAIN WINDOW CONFIG
        # -------------------------
        self.window = tk.Tk()

        self.window.title("Baby Names with Tabs")
        self.window.resizable(True, True)
        
        self.create_widgets()



    def create_widgets(self):

        # -------------------------
        # TABS
        # -------------------------
        
        self.tab_control = ttk.Notebook(self.window)
        self.tab_one = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_one, text="Tab #1")
        self.tab_two = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_two, text="Tab #2")
        self.tab_control.pack(expand=1, fill="both")
        # -------------------------
        # WIDGETS
        # -------------------------
        self.tab_frame = ttk.LabelFrame(self.tab_two, text="")
        self.tab_frame.grid(column=0, row=0)

        ttk.Label(self.tab_frame, text="Please select the files to search").grid(column=0, row=0, sticky=tk.W)
        self.tab_frame = ttk.LabelFrame(self.tab_two, text="Read from Pasted text")
        self.tab_frame.grid(column=0, row=0)
        
        
        self.scrollable_text = scrolledtext.ScrolledText(self.tab_one, width=40, height=3)
        self.scrollable_text.grid(column=0, columnspan=3, row=0)
        # self.scrollable_text.insert(tk.INSERT,"")
        
        self.btn = tk.Button(self.tab_one, text="click", command=self.create_my_thread)
        self.btn.grid(row=1, column=0)



        # -------------------------
        # Helper Methods
        # -------------------------

    def create_my_thread(self):
        self.my_thread = Thread(target=self.populate_text, args=[1,5])
        self.my_thread.setDaemon(True)
        self.my_thread.start()
        print(f'my_thread: {self.my_thread.is_alive()}')


    def populate_text(self, zzz=3, num_times=15):
        for index in range(num_times):
            sleep(zzz)
            print(index)
            self.scrollable_text.insert(tk.INSERT, str(index)+'\n')

    def in_a_thread(self):
        print("Hanging from a thread")


if __name__ == '__main__':
    my_gui = GUI()

    my_thread = Thread(target=my_gui.in_a_thread)

    my_gui.window.mainloop()