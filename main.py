import pyfirmata
import time
import tkinter as tk
# board.digital[7].write(1)
    # time.sleep(1)
    # board.digital[7].write(0)
    # time.sleep(1)
board = pyfirmata.Arduino('/dev/cu.usbmodem141301')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
pin8 = board.get_pin('d:8:s')

global_step = 10
direction = ""
running = False
jobid = None

def move_servo(step):
    global jobid
    global global_step
    global direction
    print("Moving (%s)" % step)
    if(direction=="North"):
        step+=1
    else:
        step-=1
    pin8.write(step)
    jobid = window.after(5, move_servo, step)
    global_step = step


# def handle_left(step):
#     #print
# 
# def stop_left():
#     # print

def handle_right():
    print("clicked");


def handle_top(step):
    global direction
    direction = "North"
    move_servo(step)

def stop_top():
    global jobid
    global global_step
    window.after_cancel(jobid)
    print(global_step)
    print("stopping motor...")


def handle_bottom(step):
    global direction
    direction = "South"
    move_servo(step)

def stop_bottom():
    global jobid
    global global_step
    window.after_cancel(jobid)
    print(global_step)
    print("stopping motor...")

window = tk.Tk()
window.geometry('500x500')
window.configure(bg = "#023138")
frame_a = tk.Frame(master = window,width = 500, height = 500, pady = 100, bg = "#023138")
frame_a.pack();
label = tk.Label(master = window,bg = "#023138", text = "NSA Robotics")
label.pack();
button_left = tk.Button(
    text="<",
    width=12,
    height=6,
    highlightbackground='black',
    master=frame_a
)
button_right = tk.Button(
    text=">",
    width=12,
    height=6,
    highlightbackground='black',
    command=handle_right,
    master=frame_a
)
button_top = tk.Button(
    text="^",
    width=12,
    height=6,
    master = frame_a,
    highlightbackground='black'
)
button_bottom = tk.Button(
    text="v",
    width=12,
    height=6,
    highlightbackground='black',
    master = frame_a
)
#positioning
button_left.grid(row=1, column = 0, padx = 10);
button_right.grid(row = 1, column = 2, padx = 10);
button_top.grid(row = 0, column = 1, pady = 10);
button_bottom.grid(row = 1, column = 1);
# end positioning

#binding methods
button_top.bind('<ButtonPress-1>', lambda event, step=global_step: handle_top(step))
button_top.bind('<ButtonRelease-1>', lambda event: stop_top())

button_bottom.bind('<ButtonPress-1>', lambda event, step=global_step: handle_bottom(step))
button_bottom.bind('<ButtonRelease-1>', lambda event: stop_bottom())
window.mainloop();




