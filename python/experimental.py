import math
import random
import turtle

win_length = 500
win_height = 500

turtles = 1

turtle.screensize(win_length, win_height)


class racer(object):
    def __init__(self, color, pos, angle):
        self.pos = pos
        self.ang = angle
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.hideturtle()
        self.turt.setpos(pos)
        self.turt.setheading(90)
        self.turt.pendown()
        self.turt.speed(100)

    def move(self):
        self.turt.penup
        self.turt.pendown
        self.turt.right(90)
        self.turt.forward(100)
        self.turt.back(300)
        self.turt.forward(100)
        self.turt.right(90)
        self.turt.forward(100)
        self.turt.back(200)
        self.turt.forward(200)
        self.turt.right(-90)
        self.turt.forward(-100)
        self.turt.back(-300)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)
 


def startGame():
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ['black']
    angles = [181, 90, 72, 60, 80, 176, 200, 260, 75]
    
    for t in range(turtles):
        newPosX = 0
        newPosY = 0     
        tList.append(racer(colors[t],(newPosX, newPosY), angles[t]))
    #for x in range(1,50):
        #print(x)
        for t in tList:
            t.move()


startGame()



