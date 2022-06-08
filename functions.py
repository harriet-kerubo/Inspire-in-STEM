#!/usr/bin/python

# Name : Harriet K

# Date : 31/05/2022

##############

##functions is a block of code which gets executed together

#definition of function:
def say_hello():
    print("Hello from JKUAT")
    x = 4
    y = 7
    z = x + y
    print(z)
say_hello()    

def bark():
    print("Dogs bark woof woof")
bark()    

def meow():
    print("Cats meow meow")
meow()    

def bray():
    print("Donkeys bray bray")
bray()    

def bleat():
    print("Goats bleat bleat")
bleat()    

def add_numbers(x,y):
    sum_numbers = x + y
    print("The sum of the numbers:", sum_numbers)

add_numbers(40,50)
add_numbers (200,200)
add_numbers(1,4) 

def product_numbers(x,y):
    product_numbers = x * y
    print("The product of the numbers:", product_numbers)

product_numbers(40,50)
product_numbers(200,200)
product_numbers(90,90)

##using default parameters
def print_name(name="Hariet Kerubo"):
    print(name)

print_name("Martha")    

##return from a function
def get_sum(num1,num2):
    sum_nums=num1+num2
    return sum_nums
print()    
print(get_sum(7,12))

##square of numbers
def powers(number,power):
    pow_numb=number**power
    return pow_numb
print()
print(powers(6,4))    

def get_full_name(f_name,s_name):
    full_name=f_name+" "+s_name
    return full_name.title()
print()
print(get_full_name("Harriet","Kerubo"))    

#returning a dictionary from a function
def create_full_name(first_name,second_name):
    person={'first':first_name,'second':second_name}
    return person

student=create_full_name('Harriet','Kerubo')
print(student)    

#parsing a list in a function
def greet_friends(names):
    for  name in names :
        msg = "Hello" + name . title()+"!"
        print (msg)

friends=['Edith','Andre','Tara','Harry']        
greet_friends(friends)