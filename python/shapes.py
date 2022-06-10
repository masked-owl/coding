import turtle

turtle.speed(10)
turtle.shape('turtle')
turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
# turtle.done()


turtle.speed(10)
for y in [1,2,3,4,5,6,7,8,9,10]:
    for colour in ["pink", "blue", "cyan", "magenta", "red", "yellow", "black", "gray", "green"]:
        turtle.pencolor(colour)
        turtle.color(colour)
        for x in [1,2,3]:
            turtle.forward(200)    
            turtle.right(120)
        turtle.right(5)

turtle.done()

