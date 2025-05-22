#Hello , today i created a mini project.

print("Welcome to Personal Details Formatter")

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
gender = str(input("Enter you gander: "))
salary = float(input("Enter your current salary: "))
company = str(input("Enter you company name: "))


print("So we are formating the details you provided")

def format_details(name , age , gender , salary , company):
    return f"""your name is {name}
your age is {age} 
your age is {age}
your gender is {gender}
your current salary is {salary}
your company name is {company}
"""

print(format_details(name,age,gender,salary,company))