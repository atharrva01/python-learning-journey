print("This Projects help you to get the table of any number you want.")

i = int(input("Enter the number for wihch you want the table to be printed: "))

for j in range(1,11):
    print(i,"*",j,"=",i*j)
    j +=1