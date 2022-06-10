 #!/usr/bin/python

 #Name : Harriet K

 #Date : 10 / 06 / 2022

 #Analog clock

 #importing the modules
import time
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600,height = 600)
wn.title("Simple analog clock by Harriet")
wn.tracer(0)

#Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h , m , s , pen):

    #Draw clock face 
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("purple")
    pen.pendown()
    pen.circle(250)

#Drawing lines for the hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

for _ in range(12):
    pen.fd(190)
    pen.pendown()
    pen.fd(20)
    pen.penup()
    pen.goto(0,0)
    pen.rt(30)
    
#Drawing the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("yellow")
    pen.setheading(90)    
    angle = (10 / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

#Drawing the minute hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (15 / 60) *360
    pen.rt(angle)
    pen.pendown()
    pen.fd(30)

#Drawing the second hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (50 / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(30)


draw_clock(10, 15 , 0, pen)




wn.mainloop()     