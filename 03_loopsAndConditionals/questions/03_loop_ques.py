# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter the number"))
count = 11

for i in range(1, count):
    if i == 5:
        continue
    print(num, " * ", i , " =" , num*i)
    
    