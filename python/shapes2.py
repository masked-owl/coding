import math
import random
import turtle

win_length = 500
win_height = 500

turtles = 9

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
        self.turt.showturtle()
        self.turt.setpos(pos)
        self.turt.setheading(90)
        self.turt.pendown()
        self.turt.speed(100)

    def move(self):
        self.turt.forward(70)
        self.turt.right(self.ang)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def startGame():
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", 'cyan', 'teal', 'orange', 'purple', 'black', 'pink']
    angles = [120, 90, 72, 60, 80, 176, 200, 260, 75]
    
    for t in range(turtles):
        if t < 4:
            newPosX = -260 + t*(1200)//turtles
            newPosY = -230
        elif t < 8:
            newPosX = -260 + (t-4)*(1200)//turtles
            newPosY = 200
        else:
            newPosX = 0
            newPosY = 0
            
        tList.append(racer(colors[t],(newPosX, newPosY), angles[t]))

    run = True
    while run:
    #for x in range(1,50):
        #print(x)
        for t in tList:
            t.move()


startGame()

