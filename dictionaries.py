#A dictionary is a collection of key value pairs
#syntax: dictionary = {'key' : 'value'}
names = {'John','Mary'}
colors= {'color':'red'}
vehicle= {'type':'toyota','plate_number':'KYZ954P'}
print(type(names))
print(type(colors))
print(type(vehicle))
#print(type(names)) #we use the type method to read the data

#accessing values in a dictionary
print(vehicle['type'])
print(vehicle['type' and 'plate_number'])

#You can access the value of an element inside the dictionary

#dictionary person
person = {'name':'Harriet','P_number':'0709821233','gender':'female','address':'321-0200'}
print(person['name'])
print(person['P_number'])
print(person['gender'])
print(person['name' and 'P_number' and 'gender' and 'address'])

#adding to a dictionary
person['age']='19'
print(type(person))
print(person)

print(person['name'],str(['age']))

#deleting from a dictionary
del[person ['P_number']]
print(person)

#looping over dictionaries
for key, value in person.items():
    print(f"{key}:{value}")
colors =["red" , "green" , "blue" , "purple"]

i = 1
while i < len(colors):
    if(colors[1]=='green'):
        print(colors[1].upper())
        i +=1

i = 0
while i < len(colors):
    if(colors[0]=='red'):
        print(colors[0].upper()) 
        i +=1

i = 2
while i < len(colors):
    if(colors[2]=='blue'):
        print(colors[2].upper())
        i +=1

i = 4
while i < len(colors):
    if(colors[4]=='purple'):
        print(colors[4].upper())
        i +=1





