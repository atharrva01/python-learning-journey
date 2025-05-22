#updated version of my previous version of calculator.

print("This projects is the updated version of calculator from last week.")

no_1 = int(input("Enter the number 1: "))
no_2 = int(input("Enter the number 2: "))

sum_ = lambda x,y: x+y
sub = lambda x,y: x-y
mul = lambda x,y: x*y
div = lambda x,y: x/y
mod = lambda x,y: x%y
print("So we are calculating the operation you provided")

operation =int(input("Enter the operation you want to perform: \n1.Addition\n2.Substraction\n3.division\n4.Multiplication\n5.Modulo\n"))

if(operation ==1):
    print(sum_(no_1,no_2))
elif(operation ==2):
    print(sub(no_1,no_2))
elif(operation == 3):
    print(div(no_1,no_2))
elif(operation == 4):           
    print(mul(no_1,no_2))
elif(operation == 5):
    print(mod(no_1,no_2))
else:
    print("Please enter a valid operation")
