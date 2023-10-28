from tkinter import *
import customtkinter
import numpy
import pandas as pd
from tkinter import ttk, filedialog, messagebox

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

root.title('Custom Tkinter Tree')
root.geometry('900x400')

def open_excel():
    my_file = filedialog.askopenfilename(title='Open File', filetype=(('Excel Files', '.xlsx'), ('All Files','*.*')))
    
    try:
        df = pd.read_excel(my_file)
        print(df)
    except Exception as e:
        messagebox.showerror('Woah!', f'There was a problem! {e}')
    
    my_tree.delete(*my_tree.get_children())
    
    # Get the Headers
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    
    # show the headers
    for col in my_tree['column']:
        my_tree.heading(col, text=col)
        
    # show data
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert('', 'end', values=row)

my_tree = ttk.Treeview(root)
my_tree.pack(pady=20)

my_tree.heading('#0', text='\n')

style = ttk.Style()
style.theme_use('default')

style.configure('Treeview', background='#707070', foreground='black', rowheight=25, fieldbackground='#707070')

#style.configure('Treview.Heading', )

# change color of selected row
style.map('Treeview', background=[('selected', '#535353')])

my_button = customtkinter.CTkButton(root, text='Open Excel File', command=open_excel)
my_button.pack(pady=20)

root.mainloop()
