#This is the number Analyser 
import math
number = int(input("Enter the number: "))

print("Welcome to Number Analyzer")
print("So we are analyzing the number you provided")

def sum_num(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_num(number//10)
    
print(f"The sum of number you have provided is {sum_num(number)}")

def fact_num(number):
    if number == 0 or number == 1 :
        return 1
    else:
        return fact_num(number-1) * number
    
print(f"The factorial of number you have provided is {fact_num(number)}")

square_root = math.sqrt(number)
print(f"The square root of number you have provided is {square_root}")

def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return("Odd")
    
print(f"The number you have provided is {even_odd(number)}")