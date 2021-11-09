from tkinter import *
from tkinter import colorchooser

canvas_width = 700
canvas_height = 500
brush_size = 3
color = "black"

def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def brush_size_change(new_size):
    global brush_size
    brush_size = new_size

def color_change():
    global color
    new_color = colorchooser.askcolor()
    color = new_color[1]

def eraser():
    global color
    new_color = "white"
    color = new_color

def back():
    global bg_new
    bg_new = colorchooser.askcolor()
    bg = bg_new[1]
    w = Canvas(root, bg=bg_new[1])
    w.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
    w.bind("<B1-Motion>", paint)

root = Tk()
root.title("Paint")

w = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
w.bind("<B1-Motion>", paint)

color_btn = Button(text="Color", width=10, command = lambda: color_change())
clear_btn = Button(text="Clear", width=10, command = lambda: w.delete("all"))
eraser_btn = Button(text="Eraser", width=10, command = lambda: eraser())
back_btn = Button(text="Back", width=10, command = lambda: back())


tree_btn = Button(text="3", width=10, command = lambda: brush_size_change(3))
five_btn = Button(text="5", width=10, command = lambda: brush_size_change(5))
eight_btn = Button(text="8", width=10, command = lambda: brush_size_change(8))
oneone_btn = Button(text="11", width=10, command = lambda: brush_size_change(11))
onefour_btn = Button(text="14", width=10, command = lambda: brush_size_change(14))
oneseven_btn = Button(text="17", width=10, command = lambda: brush_size_change(17))
onetwo_btn = Button(text="20", width=10, command = lambda: brush_size_change(20))

w.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)


color_btn.grid(row=0, column=0)
clear_btn.grid(row=0, column=6)
eraser_btn.grid(row=0, column=2)
back_btn.grid(row=0, column=4)

tree_btn.grid(row=1, column=0)
five_btn.grid(row=1, column=1)
eight_btn.grid(row=1, column=2)
oneone_btn.grid(row=1, column=3)
onefour_btn.grid(row=1, column=4)
oneseven_btn.grid(row=1, column=5)
onetwo_btn.grid(row=1, column=6)

root.mainloop()
