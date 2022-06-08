#!/usr/bin/python

import random
print("welcome to our password generator")
character = "HarrietBacarrrdiii"
num_passwords = int(input("How many numbers do you have?"))
len_passwords = int(input("ask user for password length"))
print(num_passwords)
print(len_passwords)
for passwords in range(num_passwords):
    passwords =" "
for c in range(len_passwords):
    passwords = random.choice(character)
    print(passwords)    

