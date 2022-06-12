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

#Importing modules
from turtle import Turtle,Screen
import datetime

#Creating window
window = Screen()
window.title("Analog clock by Harriet")
window.bgcolor("black")
window.setup(width= 400,height=300)

#Creating clock face
circle = Turtle()
circle.penup()
circle.pencolor("#118893")
circle.speed(0)
circle.pensize(20)
circle.hideturtle()
circle.goto(0,-390)
circle.pendown()
circle.fillcolor("#17202A")
circle.begin_fill()
circle.circle(300)
circle.end_fill()

#creating minute hand 
hHand =Turtle()
hHand.shape("arrow")
hHand.color("yellow")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=26)

#creating minute hand
mHand = Turtle()
mHand.shape("arrow")
mHand.color("white")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=26)

#creating second hand
sHand = Turtle()
sHand.shape("arrow")
sHand.color("pink")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=26)

#Creating center circle
centerCircle = Turtle()
centerCircle.shape("circle")
#setting color to white
centerCircle.color("white")
centerCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)

#numbers with pen
pen = Turtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h,m,s,pen):
    pen.penup()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)
    

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

for clock in range(12):
    pen.fd(190)
    pen.pendown()
    pen.fd(20)
    pen.penup() 
    pen.goto(0,0)
    pen.rt(6)



wn.mainloop()


