 #!/usr/bin/python


 #calculating the factorial of 6
number=int(input("Enter the number")) 
factorial = 1
if number <0:
     print("factorial of negative number does not exist")
elif number==0:
    print("factorial of 0 is 1")   
else :
    for i in range(1,number+1):  
      factorial = factorial *i
print("factorial of number :",factorial)
      



