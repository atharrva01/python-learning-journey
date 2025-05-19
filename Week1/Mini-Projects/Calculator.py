print("This projects helps you calculate the operation on any two numbers.")

no_1 = int(input("Enter the number 1: "))
no_2 = int(input("Enter the number 2: "))

operation =int(input("Enter the operation you want to perform: \n1.Addition\n2.Substraction\n3.division\n4.Multiplication\n5.Modulo\n"))

if(operation ==1):
    print(no_1 + no_2)
elif(operation ==2):
    print(no_1 - no_2)
elif(operation == 3):
    print(no_1 / no_2)
elif(operation == 4):           
    print(no_1 * no_2)
elif(operation == 5):
    print(no_1 % no_2)
else:
    print("Please enter a valid operation")
