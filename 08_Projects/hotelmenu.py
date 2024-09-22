menu = {
    "Pizza": 180,
    "Pasta": 90,
    "Burger": 100,
    "Coffee": 90
}
# print("Please select the option:")
print("Pizza: Rs.180 \nPasta: Rs.90 \nBurger: Rs.100 \nCoffee: Rs.90")

item_name = input("Please enter the item you want to have ")
total_amount = 0
if item_name in menu:
    total_amount += menu[item_name]
    print(f"Your item {item_name} has been added.")
else:
    print(f"Order item {item_name} is not available yet.")
 
another_order = input("Do you want to add something else? (Yes/No)")
if another_order == "Yes":
    item_name2 = input("Please enter the item you want to add")
    if item_name2 in menu:
        total_amount += menu[item_name2]
    else:
        print(f"Ordered item {item_name2} is not available yet")

print(f"Your total amount is Rs.{total_amount}. Thank you for your order.")


    
    
    

