from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')

root.title('Frame and Labels')
root.geometry('500x350')

def thing():
    my_label.config(text=my_entry.get())

my_frame = tb.Frame(root, bootstyle='light')
my_frame.pack(pady=40, fill=X, padx=20)

my_entry = tb.Entry(my_frame, font=('Helvetica', 18))
my_entry.pack(pady=20, padx=20)

my_btn = tb.Button(my_frame, text="Click Me!", bootstyle='dark', command=thing)
my_btn.pack(pady=20, padx=20)

my_label = tb.Label(root, text='Hello There!', font=('Helvetica', 18))
my_label.pack(pady=20)

root.mainloop()
