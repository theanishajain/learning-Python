# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children.
# Everyone gets a $2 discount on Wednesday.

# day = input("Enter a day please")
# age = int(input("How old are you?"))
# if day == "Wednesday":
#     price_for_adults = 12 
    # if(age)
    
    
# PROPER SOLUTION
from datetime import date
today = date.today()

age = int(input("Enter your age"))
price = 0 

if today.weekday() == 2:
    if age > 18:
        price = 12 -10
        print("WOW Welcome on Wednesday , you are eligible for the discount ", age)
    else :
        price = 8 -2
        print("WOW Welcome on Wednesday , you are eligible for the discount ", age)
else :
    if age>18:
        price = 12
        print("We welcome a humble person ", age)
    else: 
        price = 8
        print("We welcome a humble person ", age)
        
print(price)
        


    