from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename='superhero')

root.title("TTK Bootstrap! Floodgauge")
#root.iconbitmap('images/comedy.ico')
root.geometry('500x750')

def starter():
    my_gauge.start() #gauge start
    #my_gauge2.start()
    my_gauge2.configure(value = my_gauge.variable.get()) #manual update by input data

def stopper():
    my_gauge.stop()
    #my_gauge2.stop()

def incrementer():
    my_gauge.step(10)
    my_gauge2.configure(value = my_gauge.variable.get()) #manual update by input data
    my_label.config(text=f"Position: {my_gauge.variable.get()}")

my_gauge = tb.Floodgauge(root, bootstyle="success",
                         font=("Helvetica", 5),
                         mask="Pos: {}%",
                         maximum=80,
                         orient="horizontal",
                         value=10, #default value
                         mode="determinate"
                        )
my_gauge.pack(pady=50, fill=X, padx=20)

my_gauge2 = tb.Floodgauge(root, bootstyle="success",
                         font=("Helvetica", 18),
                         mask="Pos: {}%",
                         maximum=80,
                         orient="horizontal",
                         value=10,
                         mode="indeterminate"
                        )
my_gauge2.pack(fill=X, padx=50)

start_button = tb.Button(root, text="Start", bootstyle="danger outline", command=starter)
start_button.pack(pady=20)

stop_button = tb.Button(root, text="Stop", bootstyle="danger outline", command=stopper)
stop_button.pack(pady=20)

inc_button = tb.Button(root, text="Increment", bootstyle="danger outline", command=incrementer)
inc_button.pack(pady=20)

my_label = tb.Label(root, text="Position: ")
my_label.pack(pady=20)

# Progress Menu Frame
def prg_incre():
    my_progress.step(10)
    #my_progress['value'] += 10
    my_label.config(text=my_progress['value'])

def prg_start():
    my_progress.start(10)

def prg_stop():
    my_progress.stop()

def prg_auto():
    for x in range(5):
        my_progress.step(10)
        my_label.config(text=my_progress['value'])
        
        # do context switching
        root.update_idletasks()
        # increment after 1sec
        time.sleep(1)

my_progress = tb.Progressbar(root, bootstyle='danger striped', 
                                maximum = 100,
                                mode="determinate",
                                #length = 200,
                                value = 0)

my_progress.pack(pady=20, fill=X, padx = 20)

my_frame = tb.Frame(root)
my_frame.pack(pady=20)

my_button = tb.Button(my_frame, text="PrgInc", bootstyle="info", command = prg_incre)                         
my_button.grid(column=0, row=0, padx=10)

my_start_button = tb.Button(my_frame, text="PrgStart", bootstyle="info", command = prg_start)
my_start_button.grid(column=1, row=0, padx=10)

my_stop_button = tb.Button(my_frame, text="PrgStop", bootstyle="info", command = prg_stop)
my_stop_button.grid(column=2, row=0, padx=10)

my_auto_button = tb.Button(my_frame, text="PrgAuto", bootstyle="info", command = prg_auto)
my_auto_button.grid(column=3, row=0, padx=10)

my_label = tb.Label(root, text='')
my_label.pack(pady=20)

root.mainloop()