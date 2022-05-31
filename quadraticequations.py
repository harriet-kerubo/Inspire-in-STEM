#!/usr/bin/python

######
# Name : Harriet 
# Date : 31/5/2022

##############
import math

a =int(input("Enter the constant of the first term"))
b =int(input("Enter the constant of the second term"))
c =int(input("Enter the constant of the first term"))
w = math.sqrt((b**2)-4*a*c)

y_1 = (-b + w)/2*a
y_2 = (-b - w)/2*a

print("The roots of the quadratic equation are :",y_1,y_2)    
