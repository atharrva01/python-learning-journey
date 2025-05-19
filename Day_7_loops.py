#Here we are staring with loops.
#we will use loop for writing something multiple times 



#here we will write loop to print natural numbers from 1 t 100

for i in range(1,1001):
    print(i)
    i += 1

for i in range(1,50):
    if(i % 2 == 0):
        print(i) #this will return me even numbers between 1-50
    i = i+1

#this loop will return prime numbers from 1-50
for i in range(1,50):
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        print(i) #this will return me prime numbers between 1-50
    i = i+1
    
a=int(input("Enter a number: "))
while a>10:
   
    print(a)    
    print("Hello World!")
    break
else:
    print("Enter the value greater than 10 for result.")
    
