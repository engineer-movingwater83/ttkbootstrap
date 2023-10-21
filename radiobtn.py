from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')

root.title('Ridio Btn!')
root.geometry('500x600')

# Clicker Function
def clicker():
    my_label.config(text=f'You Selected: {my_topping.get()}')

def radioClick():
    my_label.config(text=f'You Selected: {my_topping.get()}')

# Create Radio Button List
toppings = ["Pepperoni", "Cheese", "Veggie"]

# Create A Tkinter Variable to Keep Track of everything
my_topping = StringVar()

for topping in toppings:
    tb.Radiobutton(root, bootstyle='danger', variable=my_topping, text=topping, value=topping, command=radioClick).pack(pady=20)
    #value : this radio button has this value
    #variable = if this radio button is clicked, this radio "value" is saved into "variable"

# Create button
my_button = tb.Button(root, text='ClickMe', command=clicker)
my_button.pack(pady=20)

# Create a Label
my_label = tb.Label(root, text='You Selected: ')
my_label.pack(pady=20)

# Create actual Radio Button Buttons
rb1 = tb.Radiobutton(root, bootstyle='info toolbutton', variable=my_topping, text='Radio Button1', value='Radio Btn1', command=radioClick).pack(pady=20)
rb2 = tb.Radiobutton(root, bootstyle='info toolbutton outline', variable=my_topping, text='Radio Button2', value='Radio Btn2', command=radioClick).pack(pady=20)
#button style can be different


root.mainloop()

