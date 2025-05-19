#Here i learnt about Type Casting, where we convert the data type of a variable to another data type.

age = (input("Enter Your Age: "))
print(age)
print(type(age)) #this will return as string even if we input a number
age_int = int(input("Enter a number: ")) #this will convert the string to integer 
print(age_int)
print(type(age_int)) #this will return as integer