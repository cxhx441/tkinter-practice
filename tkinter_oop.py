import tkinter as tk
from tkinter import messagebox
# # BASIC WAY
# root = tk.Tk()
# root.mainloop()

# OOP WAY
class App(tk.Tk): # SHOULD HAVE ONLY ONE OF THESE INSTANCES
    def __init__(self):
        super().__init__()
        self.title('OOP Main Window Title')
        self.resizable(True, False)
        self.geometry('600x400+1600+400')
        self.attributes('-alpha', 0.8)
        self.label = tk.Label(self, text='this is my label')
        self.label.pack()
        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()
    def button_clicked(self):
        messagebox.showinfo(title='Information', message='hello, tkinter pals')

def main():
    app = App()  # SHOULD HAVE ONLY ONE OF THESE INSTANCES
    app.mainloop()

if __name__ == '__main__':
    main()