#importing modules
import turtle
import time

#creating window
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=500, height=500)
wn.title('Analog clock by Harriet')
wn.tracer(0)

#creating the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h,m,s,pen):

#drawing clock face    
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color('green')
    pen.pendown()
    pen.circle(210)

#drawing hour hand
    pen.up()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.up()
        pen.goto(0,0)
        pen.rt(30)

