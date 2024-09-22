# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

num = input("Enter your age ")
age= int(num)

if age<13:
    print("You are a child", age)
elif  age<=19:
    print("You are a teenager", age)
elif  age<=59:
    print("You are an adult", age)
else:
    print("you ara a senior", age)
    

    