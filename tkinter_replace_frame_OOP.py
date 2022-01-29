import tkinter as tk


class InputFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # grid layout for input frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        # Find what
        tk.Label(self, text='Find what:').grid(column=0, row=0, sticky=tk.W)
        keyword = tk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        # Replace with
        tk.Label(self, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
        replacement = tk.Entry(self, width=30)
        replacement.grid(column=1, row=1, sticky=tk.W)

        # Match Case checkbox
        match_case = tk.StringVar()
        match_case_check = tk.Checkbutton(self, text='Match case', variable=match_case, command=lambda: print(match_case.get()))
        match_case_check.grid(column=0, row=2, sticky=tk.W)

        #Wrap Around checkbox
        wrap_around = tk.StringVar()
        wrap_around_check = tk.Checkbutton(self, text='Wrap around', variable=wrap_around, command=lambda: print(wrap_around.get()))
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

class ButtonFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)

        self.create_widgets()
    
    def create_widgets(self):
        tk.Button(self, text='Find Next').grid(column=1, row=0)
        tk.Button(self, text='Replace').grid(column=0, row=1)
        tk.Button(self, text='Replace All').grid(column=0, row=2)
        tk.Button(self, text='Cancel').grid(column=0, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #root window
        self.title('Replace')
        self.geometry('400x150+1600+800')
        self.resizable(False, False)
        #windows only (remove the minimize/maximize button)
        self.attributes('-toolwindow', True)

        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):
            #Layout on the root window
            input_frame = InputFrame(self)
            input_frame.grid(column=0, row=0)

            button_frame = ButtonFrame(self)
            button_frame.grid(column=1, row=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()