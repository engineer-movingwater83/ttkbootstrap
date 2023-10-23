import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

def plot():
    ax.clear()
    ax2.clear()
    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    ax.scatter(x, y)
    ax2.plot(x, y, 2)
    canvas.draw()


root = tk.Tk()
fig = plt.Figure() # make new figure block
ax = fig.add_subplot(2, 1, 1) # make 2 row, 1col sub plot and return first plot
ax2 = fig.add_subplot(2, 1, 2) # make 2 row, 1col sub plot and return second plot

#fig, ax = plt.subplots()

label = tk.Label(text = 'Matplot')
label.config(font=('Courier', 32))
label.pack()

frame = tk.Frame(root, background='black') # make new frame

canvas = FigureCanvasTkAgg(fig, frame) # make canvas object which will used for draw 

canvas.get_tk_widget().pack()
#canvas.get_tk_widget().pack(fill='x')
frame.pack(fill='x')

tk.Button(frame, text = 'Plot Graph', command = plot).pack(pady = 10)

root.mainloop()

# from tkinter import *
# import numpy as np
# import matplotlib.pyplot as plt

# root = Tk()
# root.title('PyPlot')

# root.geometry('400x200')

# def graph():
#     house_price = np.random.normal(200000, 25000, 5000)
#     plt.hist(house_price, 50)
#     plt.show()
    
# my_button = Button(root, text='Graph', command=graph)
# my_button.pack()

# root.mainloop()
