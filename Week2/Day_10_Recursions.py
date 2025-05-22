#Today i learnt about Recursions 
# 0 1 1 2 3 5
# 1 1 2 3 4 5 


def fib(n):
    if(n==0 or n==1):
        return n
    else:
       return fib(n-1) + fib(n-2)

print(fib(3))

'''
factorail(1) = 1
fact(2) = fac(1) * 2 
fac(3) = fac(2) * 3
factorial(4) = fac(3) * 4
factorial(5) = fac(4) * 5
fac(n) = fac(n-1) * n



'''
def factorial(n):
    if (n==0 or n==1):
         return (1)
    else:
         return (n *factorial(n-1))

print(factorial(4))

#I am solving a question which creates a func that return the sum of first n natural numbers

'''
sum(1) = 1
sum(2)= sum(1) + 2
sum(3) = sum(2)) + 3
sum(n) = sum(n-1) + n

'''

def sum(n):
    if(n==0 or n==1):
        return n
    else:
        return sum(n-1)+ n
    
print(sum(50))

#in this question i am trying to find the sum of digits in a number

'''
12345 = 1 + 2 + 3 + 4 + 5



'''

def sum_digits(n):
    if n==0 :
        return 0 
    else:
        return n%10 + sum_digits(n//10)
    
print(sum_digits(123499898985))

