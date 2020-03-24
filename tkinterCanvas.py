from tkinter import *
import random
import time
from PIL import ImageTk, Image

root = Tk()

# create title for tkinter
root.title("Canvas")

# set up background
root.geometry("300x300")
c = Canvas(root, bg="lightblue")
c.pack()

# create line
l = c.create_line(0, 0, 300, 300, width=200, fill="white")

# create circle
o = c.create_oval(130, 170, 170, 130, fill="lightyellow")

# polygon
p = c.create_polygon(100, 150, 150, 200, 200, 150, 175,100, 125, 100, fill="lightblue")

# ————————————————————————————————————————————————————————————————————————
# insert image

# img = ImageTk.PhotoImage(Image.open("C:/Users/92475/Pictures/zhdwm2.jpg"))
# image=Label(c, image=img)
# image.pack()

# filename = PhotoImage(file = r"C:\Users\92475\Pictures\Each.png")
# image = c.create_image(c, 30, 30, anchor=NE, image=filename)
# _________________________________________________________________________

# create shape using function
def create_rectangle(x1, y1, x2, y2):
    c.create_rectangle(x1, y1, x2, y2, fill="lightgreen")

create_rectangle(0, 20, 20, 0)
create_rectangle(300, 20, 280, 0)

#random rec

def randomrec(num):
    for i in range (0, num):
        x1 = random.randrange(150)
        x2 = x1 + random.randrange(150)
        y1 = random.randrange(150)
        y2 = y1 + random.randrange(150)
        c.create_rectangle(x1, y1, x2, y2)

randomrec(10)

 #create text

c.create_text(150, 150, text="YOZA", font="Arial, 30")

#animation

triangle = c.create_polygon(10, 10, 10, 60, 50, 35 )
for i in range (0, 60):
    c.move(triangle, 1, 0)
    root.update()
    time.sleep(0.1)






root.mainloop()
