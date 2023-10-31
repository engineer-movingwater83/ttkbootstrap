import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SlidePanel(ttk.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent, bootstyle=DANGER)
        
        self.start_pos = start_pos + 0.05
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)
        #print(self.width)
        
        # animate logc
        self.pos = self.start_pos
        self.in_start_pos = True
        
        # layout
        self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
    
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()
            
    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animate_forward)
            
        else:
            self.in_start_pos = False
            
    def animate_backward(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animate_backward)
            
        else:
            self.in_start_pos = True
        
                

root = ttk.Window()
root.geometry('600x400')

animated_panel = SlidePanel(root, 0, -0.3)

b2 = ttk.Button(animated_panel, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side = TOP, padx=5, pady=10)

b3 = ttk.Button(animated_panel, text="Button 2", bootstyle=(INFO, OUTLINE))
b3.pack(side = TOP, expand = True, fill = 'both', padx=5, pady=10)


button_x = 0.5
button = ttk.Button(root, text="Button 1", command = animated_panel.animate, bootstyle=SUCCESS) 
button.place(relx = button_x, rely = 0.5, anchor = 'center')

root.mainloop()