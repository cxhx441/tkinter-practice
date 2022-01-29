import tkinter as tk
from tkinter import messagebox

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label
        self.label = tk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

        # show the frame on the container
        self.pack()

    def button_clicked(self):
        messagebox.showinfo(title='Information',
                 message='Hello, Tkinter!')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('my App Window')
        self.geometry('300x100+1600+800')

if __name__ == '__main__':
    app = App()
    frame = MainFrame(app)
    app.mainloop()