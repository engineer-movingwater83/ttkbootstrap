from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')

root.title('EntryBox')

root.geometry('500x350')

def speak():
    my_label.config(text=f'You Typed: {my_entry.get()}')

my_entry = tb.Entry(root, bootstyle='success', font=('Helvetica', 18), width=5, show='*')
my_entry.pack(pady = 50)

my_btn = tb.Button(root, bootstyle='danger outline', text='Click Me', command=speak)
my_btn.pack(pady=20)

my_label = tb.Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
