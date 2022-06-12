#Making a simple calculator
print("Select an operation to perform:")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")
operation = input()

if operation == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter the first number: ")   
    num2 = input("Enter the first number: ")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the first number: ") 
    print("The product is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the first number: ")
    print("The result is " + str(int(num1) / int(num2)))
else:
    print("The invalid Entry")    