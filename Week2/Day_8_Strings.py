
name = "Atharva"
name_1 = 'Hello'
name_2  = """This is 3rd example of string""" #we can also write strings in triple quotes this is used when we wanted to add multiline string.
name_3 = '''So this is
me 
and i can 
write anything
in any line but in between these three quotes'''

print(type(name))
print(type(name_3))
print(name_3)

#Strings are immutable , which means they cant be changed.

#So here we will learn about string methods like indexing , slicing , concatenation,formating , f strings & doc strings.

#1.String Indexing
print("We are performing String Indexing")
name = "Atharva"
print(name[3])
print(name[5])
print(name[0])

#2.String Slicing
print("Here we are doing String Slicing")
name_1 = "Hello World , this is Atharva's Program"
print(name_1[0:11])
print(name_1[22:30])

#3.String Concatenation
print("This is string concatenation")
first_name = "Atharva "
last_name="Borade "
middle_name = "Ramesh "

my_full_name =( first_name   + middle_name      + last_name)
print(my_full_name)

#4.Straing Formatiing
print("String Formating , I will be using f strings here")
username = str(input("Enter you name: "))
age = int(input("Enter you age: "))
print(f"Hello {username} you have successfully entered in the system, oh and congrats you are going to turn {age + 1} next year")

#Here i will learn the functions of sting which are as follows:

name = "my name is Atharva"
print(len(name))

print(name.lower()) #this converts the complete text to lower case
print(name.upper()) #this will covert complete text/string into upper case
print(name.replace("A","K")) #this will repalce all the "A" charecters with "K"
print(name.split()) #this will split the string into list of words
