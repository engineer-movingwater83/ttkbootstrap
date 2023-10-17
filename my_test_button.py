import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def OnBtnClicked(text):
    print("Btn Clicked " + text)

root = ttk.Window(themename="darkly")

b1 = ttk.Button(root, text="Button 1", command = lambda:OnBtnClicked("b1"), bootstyle=SUCCESS) # in case of passing argument(ex. b1), need to use lambda
b1.pack(side = LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", command = lambda:OnBtnClicked("b2"), bootstyle=(INFO, OUTLINE))
b2.pack(side = LEFT, padx=5, pady=10)

root.mainloop()
