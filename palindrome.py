#!/usr/bin/python

#Name : Harriet K
#Date : 08/06/2022

string = input("Select which input to check number or letter")
if(string==string[::-1]):
    print("The letter is a palindrome")
else:
    print("The letter is not a palindrome")  
