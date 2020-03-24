# To view the keymap configuration, open the Settings/Preferences dialog Ctrl+Alt+S and select Keymap.

# declaring a variable in a class (outside of a function) : all class functions can access it
# declaring a variable inside a function inside a class : only that function can access it (its in that functions scope)
# declaring a variable with self.(variable name) inside a function inside a class : all class functions can access it
# and since everything is public, so everything accessible from inside a class is accessible from outside the class.

# Class variables can be modified by referring to them by class name (e.g. Class.x = 5) and all instances will
# inherit these changes

from tkinter import *
import time
import random

root = Tk()

c = Canvas(root, width=500, height=500, bg="lightblue", bd=1)
root.title("Bounce!")
root.resizable(0, 0)  # window size stay as it is
root.wm_attributes("-topmost", 1)  # window stay in front
root.update()
c.pack()


# create class

class ball:  # initialization
    def __init__(self, c, color, paddle):
        self.c = c  # We have initialised canvas...
        self.id = c.create_oval(10, 10, 25, 25, fill=color)  # creating the ball itself
        change_direction = [-3, -2, -1, 1, 2, 3]  # create a list of values
        random.shuffle(change_direction)  # shuffle values
        self.x = change_direction[0]  # make x change random direction
        self.y = -3
        self.c.move(self.id, 250, 250)  # start position, self y x is to change the rate flexibility
        self.c_height = self.c.winfo_height()  # get the height value in canvas
        self.paddle = paddle
        self.hit_bottom = False  # initialily it does not hit bottom

    def hit(self, pos):  # check if ball is hit

        paddle_pos = self.c.coords(self.paddle.id)
        if pos[3] <= paddle_pos[3] and pos[1] >= paddle_pos[1]:
            if pos[2] <= paddle_pos[2]:
                return True
            return False


    def draw(self):  # this is for animation, movement
        self.c.move(self.id, self.x, self.y)  # ...so we have to say self. Every time we want to use canvas
        # move function always have 3 parameters, object, x, and y, minus one = -1, we use selfxy so that it can changed
        pos = self.c.coords(
            self.id)  # this returns the coordinate[x1, y1, x2, y2] of "self id" and store it in a variable
        print(self.c.coords(self.paddle.id))
        if self.hit(pos) == True:  # use return value of another fuction to decide whether reflect or not
            self.x = 3# if wonder about the argument, it calls hit function here with the pos variable in this fuction
        if pos[1] <= 0:  # 这个是y1的值
            self.y = 3
        if pos[3] >= 500:  # this is y2
            self.y = -3
        if pos[0] <= 0:
            self.hit_bottom = True  # if ball hits x=0, hit bottom is now true, note that self hit bottom can be used here
            c.create_text(250, 250, text="Game over", font="Times, 30") #simply creates text, no association with class

        if pos[0] >= 500:
            self.x = -3

    # def score(self, hit, score):
    #
    #     if hit == True:
    #         score = score + 1
    #
    #     return score



# create a paddle which is rectangular, able to move with arrow key, if ball hits paddle, reflects.
class paddle:
    def __init__(self, c, color, playerno):
        self.c = c  # create instance
        self.y = 0
        self.id = c.create_rectangle(0, 0, 20, 100, fill=color)
        self.c.move(self.id, 30, 270)
        self.c.bind_all("<Key-Up>", self.up)  # bind up function with up key
        self.c.bind_all("<Key-Down>", self.down)

    def draw(self):  # if this function is not activated, then the object won't move
        self.c.move(self.id, 0, self.y)
        pos = self.c.coords(self.id)
        if pos[1] >= 400:
            self.y = 0
        if pos[3] <= 100:
            self.y = 0

    def up(self, event):
        self.y = -3

    def down(self, event):
        self.y = 3


paddle1 = paddle(c, "yellow", 2)  # pass in parameters, create a paddle

# paddle2 = paddle(c, "green", 2)

# ————————————————————————————————————————————
# ball2 = c.create_oval(10, 10, 25, 25)
# def drawandmove():
#     global ball2
#     c.move(ball2, 0, -1)
#     root.update()
#
# button = Button(root, command=drawandmove)
# button.pack()
# ————————————————————————————————————————————

ball2 = ball(c, "red", paddle1)  # this comes front as in while loop, ball2 func is first called
ball = ball(c, "blue", paddle1)  # create ball out of class, assign it to a variable for use


while True:
    if ball.hit_bottom is False and ball2.hit_bottom is False:  # if the hit bottom variable in the ball class is false, then ..
        ball.draw()  # call the draw function in the loop, since hit function is used IN draw function, we dont call
        # hit here
        ball2.draw()
        paddle1.draw()  # add the paddle function

    root.update_idletasks()  # so normally these two updates needs to be together
    root.update()
    time.sleep(0.01)

root.mainloop()
