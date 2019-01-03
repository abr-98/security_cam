import tkinter as tk
from subprocess import call
from tkinter import messagebox
import time,datetime
root = tk.Tk()
running = False
timer=tk.StringVar()
mytime=0
s=0
c=0
def get_value():
    try:
        mytime=int(timer.get())
    except:
         messagebox.showerror(
                 "Input NOT valid.",
                 "Please try again and enter a valid input."
             )

    #t=''.join(counter)
    #time=int(t)
    #time=time*1000
    start.config(state="normal")
    stop.config(state="normal")
def exec_cam_capture():
    global running,t,p
    t1= int(round(time.time()))
    #stop.config(state="normal")
    if running:
        t2= int(round(time.time()))
        if t2-t1==mytime:
           exit_code = call("python3 test_capture.py", shell=True)
    root.after(mytime,exec_cam_capture)



def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False
    root.destroy()
    exit_code=call("python3 main_control.py",shell=True)
    #exec_cam_capture()

def start():
    """Enable scanning by setting the global flag to True."""
    global running

    running = True
    exec_cam_capture()

frame = tk.Frame(root)
frame.pack()
root.title("Control Panel")
root.geometry('500x500')
label_1 = tk.Label(frame, text="Timer(in seconds)",width=20,font=("bold", 10))
label_1.place(x=30,y=25)
entry_1 = tk.Entry(root,textvariable=timer)
entry_1.place(x=170,y=45)
set=tk.Button(frame, text='Set',width=12,pady=10,command=get_value)
set.pack(pady=75)

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   width=25,
                   pady=10,
                   command=quit)
#button.place(x=90,y=90)
button.pack(pady=15)
start = tk.Button(frame,
                   text="Start Cam",
                   width=25,
                   pady=10,
                   state="disabled",
                   command=start)
#button.place(x=90,y=120)
#if c==0:

#start.config(state="normal")

start.pack(pady=15)

stop = tk.Button(frame,
                   text="Stop",
                   width=25,
                   pady=10,
                   state="disabled",
                   command=stop)
#if s==0:
    #stop.config(state="disabled")
#button.place(x=90,y=120)
stop.pack(pady=15)
#root.after(time, exec_cam_capture)

root.mainloop()
