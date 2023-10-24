from tkinter import *
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

root.title('Custom Tkinter Switch')
root.geometry('700x300')

def switcher():
    my_label.configure(text=swtich_var.get())

def clicker():
    my_switch.toggle()
    #my_switch.select()
    #my_switch.deselect()

swtich_var = customtkinter.StringVar(value='on')

my_switch = customtkinter.CTkSwitch(root, text='Switch', command=switcher, variable=swtich_var, onvalue='on', offvalue='off', 
                                    switch_width=200,
                                    switch_height=25,
                                    #corner_radius=1
                                    border_color='orange'
                                    )
my_switch.pack(pady=40)

my_label = customtkinter.CTkLabel(root, text='on')
my_label.pack(pady=10)

my_button = customtkinter.CTkButton(root, text='Click Me', command=clicker)
my_button.pack(pady=10)

root.mainloop()
