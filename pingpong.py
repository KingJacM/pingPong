from tkinter import *
import random
import time

root = Tk()

# background
c = Canvas(root, width = 1000, height = 500, bg = "darkgreen")
c.pack()

c.create_line(500, 500, 500, 0, width=15, fill ="black")
c.create_line(0, 0, 0, 500, width=15, fill ="black")
c.create_line(0, 500, 1000, 500, width=15, fill ="black")
c.create_line(500, 0, 500, 1000, width=15, fill ="black")
c.create_line(1000, 500, 1000, 0, width=15, fill ="black")


# def restart():
#     restart = Button(root, text="Restart", command = start)
#     restart.pack()


# create a ball
def start():
    l = Label(root, text = "Score: 0", font="Arial, 36")
    l.pack()

    class ball:

        def __init__(self, color,  pp, score_label): #design the bal
            self.c = c
            self.id = c.create_oval(0, 0, 30, 30, fill=color)
            self.c.move(self.id, 500, 250)
            self.x = 8
            direction = [-3, -2, -1, 1, 2, 3]
            random.shuffle(direction)
            self.y = direction[0]
            self.pp = pp  # create instance
            self.hit_bottom = False
            self.point = 0   #error: object not callable, solve: do not name a var and a function equal
            self.label = score_label

        def hit(self, pos):  # this will be called in move(), not individually
            pp = c.coords(self.pp.id) #get the coords of paddle, out of range because didn't add id??
            if pos[0] <= pp[2]:
                if pos[3] <= pp[3] and pos[1] >= pp[1]:
                    return True

            return False

        def animation(self): #let it move
            c.move(self.id, self.x, self.y)
            pos = c.coords(self.id)
            if pos[0] <= 20:
                self.x = 0
                self.y = 0

                self.hit_bottom == True
                c.create_text(500, 250, text="Game Over", font="Arial, 50")
                # restart()
            if pos[2] >= 1000:
                self.x = -8
            if pos[1] <= 0:
                self.y = 5
            if pos[3] >= 500:
                self.y = -5
            if self.hit(pos) == True: #add reaction here
                self.x = 8

        def score(self):

            pos = c.coords(self.id)
            if pos[0] >= 970:
                self.point += 1
                self.label.config(text="score: {}".format(self.point))

        def hit_bottom(self):
            pos = c.coords(self.id)
            if pos[0] <= 10:
                return True




    # paddle
    class paddle:

        def __init__(self, color): #add a pp parameteer to pass in paddle information
            self.c = c
            self.id = c.create_rectangle(0,0,25,125,fill=color)
            self.c.move(self.id, 25, 250)
            self.x =0
            self.y =0 #0 as initial speed is 0
            self.c.bind_all("<Key-Up>", self.up)  # bind up moving function with up key
            self.c.bind_all("<Key-Down>", self.down)



        def move(self): # to actually move the paddle, this func gets activated
            c.move(self.id, self.x, self.y)
            pos = c.coords(self.id)
            if pos[1] <= 0:
                self.y = 0
            if pos[3] >= 500:
                self.y = 0






        def up(self, event): #use this to move up
            self.y = -5

        def down(self, event):
            self.y = 5



    paddle = paddle("red")


    ball = ball("orange", paddle, l)

    while True:
        if ball.hit_bottom is False:
            ball.animation()
            paddle.move()
            ball.score()
        root.update_idletasks()
        root.update()
        time.sleep(0.01)

start()
root.mainloop()