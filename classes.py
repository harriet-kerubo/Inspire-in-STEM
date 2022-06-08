#!/usr/bin/python

##Name : Harriet K
##Date : 02/06/2022
#oriented object programming(OOP)

class Person :

 def __init__(self, _name, _age):
    self.name= _name
    self.age = _age
 def sayHi(self):
     print("Hello,my name is" +str(self.name) "I am" +str(self.age) "years old")
person1 = Person('John', 20)
person1.sayHi()

person2 = Person('James', 10)
person2.sayHi()

class Vehicle:
   def __init__(self,mileage,max_speed):
      Vehicle.max_speed=max_speed
      Vehicle.mileage=mileage
toyota=Vehicle('300km/hr',400)
print(toyota.mileage,toyota.max_speed)
 

        
   
