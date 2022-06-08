#!/usr/bin/python
#Name : Harriet  K
#Date : 06 / 06 / 2022

f = open("lesson1.txt",'x')
with open("lesson1.txt",'w') as f:
    f.write("This is my new file\n")
    f.write("I am from Syokimau\n")
    f.write("Today is a cold day\n")
#reading the file
print(f.write())
f.close()

#read line by line 
print(f.read())
print(f.readline())