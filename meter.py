from tkinter import *
import ttkbootstrap as tb

#fail....

root = tb.Window(themename='superhero')

root.title('Meter!')
root.geometry('500x550')

my_meter = tb.Meter(root)
# root, bootstyle='danger',
#                     subtext='Learn',
#                     interactive=True, #it is working with mouse drag-drop also.
#                     textright='%',
#                     textleft='$'
#                     )
my_meter.pack()

root.mainloop()