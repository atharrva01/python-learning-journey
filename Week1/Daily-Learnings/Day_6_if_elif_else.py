#I learnt about control flow like , if , elif , else statements and loops.

age = int(input("Enter your age: "))
print("Your age is: ",age)

if (age > 18):
    print("You are eligible to do anything \nfor eg. Driving,Voting etc.")
elif(age == 18):
    print("You need to verify yourself by giving few exams")
else:
    print("you are not eligible")
