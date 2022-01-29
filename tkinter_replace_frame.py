import tkinter as tk

def create_input_frame(container):
    frame = tk.Frame(container)

    # grid layout for input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    tk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
    keyword = tk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    # Replace with
    tk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = tk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = tk.Checkbutton(frame, text='Match case', variable=match_case, command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    #Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = tk.Checkbutton(frame, text='Wrap around', variable=wrap_around, command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)


    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)
    
    return frame


def create_button_frame(container):
    frame = tk.Frame(container)

    frame.columnconfigure(0, weight=1)
    tk.Button(frame, text='Find Next').grid(column=1, row=0)
    tk.Button(frame, text='Replace').grid(column=0, row=1)
    tk.Button(frame, text='Replace All').grid(column=0, row=2)
    tk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)
    
    return frame

def create_main_window():

    #root window
    root = tk.Tk()
    root.title('Replace')
    root.geometry('400x150+1600+800')
    root.resizable(False, False)
    #windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)

    #Layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()

if __name__ == '__main__':
    create_main_window()