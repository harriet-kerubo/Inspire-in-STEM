#Learning about lists
motocycle_owner = "Mojo Jojo"
plate_number = ["H1234" , "Y1234" , "S1234"]
motocycle = ["hondo" , "suzuki" , "yohanda"]
print(motocycle)

#accesing lists using git index
motocycle[1] = "Bugatti" #changing elements on a list
print(motocycle)
print(("I love")) + str(motocycle[1])

#adding items to the list
motocycle .append("Bugatti")
print(motocycle)

#task ---print the plate numbers
print(plate_number)
print(motocycle[0]) ,plate_number[0] ,motocycle[1] ,plate_number[1] , motocycle[2] , plate_number[2] 

#Deleting an item from a list -- del
del motocycle[2]
print(motocycle)
popped_motocycle = motocycle.pop()
print(motocycle)
print(popped_motocycle)

#task print a statement: My name is Mojo Jojo and I own a motocycle plate_number
print("My name is" + motocycle_owner , "and I own a motocycle" +motocycle[1] , plate_number[1] )
print(f"My name is {motocycle_owner} and I own {motocycle[1]} , {plate_number(1)}")
print(f"My name is {motocycle_owner} and I own {motocycle[1]} , plate_number[1]")

#removing an item from a list
motocycle.remove("suzuki")
print(motocycle)
