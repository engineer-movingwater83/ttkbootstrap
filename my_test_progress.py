import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import threading, time

root = ttk.Window(themename="darkly")

global currProgrss
currProgrss = 0.0

 ## progress bar
progressbar = ttk.Progressbar(
    master=root, 
    mode=INDETERMINATE,
    variable=currProgrss,
    bootstyle=(STRIPED, SUCCESS)
)

def progressbar_update(root):
    global currProgrss
    print("val = ", currProgrss)
    if(currProgrss < 100.0):
        currProgrss += 1.0
        progressbar.update();
        root.after(1000, progressbar_update(root))
    

progressbar.pack(fill=X, expand=YES)

progressbar_update(root)

root.mainloop()
