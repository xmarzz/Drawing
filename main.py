from turtle import*
import turtle

def myTurtle():
    sides=str(23)
    loops=str(450)
    pen=1

    for i in range(int(loops)):
        forward((i*2)/int(sides)+i)
        left(360/int(sides)+.360)
        hideturtle()
        pensize(pen)
        speed(30)
        left(90)

myTurtle()
turtle.done() 