import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')  # WIDTHxHEIGHT+-XPAD+-YPAD

# to center
def center_window(root):
    win_width, win_height = 600, 400

    # get screen dims
    print(win_width)
    print(win_height)

    my_screen_width = root.winfo_screenwidth()
    my_screen_height = root.winfo_screenheight()
    # find center
    center_x = int(my_screen_width/2 - win_width/2)
    center_y = int(my_screen_height/2 - win_height/2)
    # update win geometry
    root.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')

center_window(root)

# changing the resizability options
root.resizable(True, True)
root.resizable(False, False)
root.resizable(True, False)

# changing allowable min / max win sizes
min_width, min_height = 300, 200
max_width, max_height = 1200, 800
root.minsize(min_width, min_height)
root.maxsize(max_width, max_height)

# transparency
root.attributes('-alpha', 0.7)  # can't think of a reason to use this... 0.0 is fully transparent, 1.0 is opaque

# window stacking order
root.attributes('-topmost', 1)

# changing the default icon
root.iconbitmap("mman.ico")  # use a .ico image within the folder

root.mainloop()
