#So today I learnt about 2 things which are as follows : 


print("1.Variable scope")
print('Ther eare 2 types of variable scop ewhich are Global and Local scope')

name = "Athavrva" # this is a global scope which means it can be used anywhere in the program

def print_name():  
    name = "Atharv" # this is a local scope which means it can be used only in this function
    print(name) # this will print the local variable name   


#2. dOC_STRINGS

def print_name():       
    """This function prints the name of the person"""
    name = "Atharv" # this is a local scope which means it can be used only in this function
    print(name) # this will print the local variable name

print(print_name.__doc__) # this will print the docstring of the function
