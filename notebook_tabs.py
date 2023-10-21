from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')

root.title('Notebook Tabs!')
root.geometry('500x400')

my_notebook = tb.Notebook(root, bootstyle='info') # make note book
my_notebook.pack(pady=20)

frame1 = tb.Frame(my_notebook) #make frame
frame2 = tb.Frame(my_notebook) #make frame

my_label = Label(frame1, text='MyLabel', font=('Helvetica', 18)) # add label into frame1
my_label.pack(pady=20)

my_text = Text(frame1, width=70, height=10) #add text window into frame1
my_text.pack(pady=10, padx=10)

my_button = tb.Button(frame1, text='ClickMe', bootstyle='danger outline') # add button into frame1
my_button.pack(pady=20)

my_label2 = Label(frame2, text='MyLabel2', font=('Helvetica', 18)) # add label into frame2
my_label2.pack(pady=20)

#Add our frame to the notebook
my_notebook.add(frame1, text="Tab One") #attach frame1 into notebook
my_notebook.add(frame2, text="Tab Two") #attach frame2 into notebook

root.mainloop()
