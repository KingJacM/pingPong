from tkinter import *
import random
import time

root = Tk()

c = Canvas(root, width=500, height=500, bg="lightyellow")
c.pack()

ball = c.create_oval(230,270,270,230,fill="lightblue")
x_speed = 1
y_speed = 0


while True:
    c.move(ball, x_speed, y_speed)
    root.update()
    time.sleep(0.1)

root.mainloop()