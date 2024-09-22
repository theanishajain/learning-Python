# 4. Reverse a String
# Problem: Reverse a string using a loop.

str = input("Enter your string")
store_rev_str=""
length = len(str)
# reverse
# esrever
# lst = []
index = length - 1

while index >=0:
    char = str[index]
    store_rev_str = store_rev_str + char
    index = index -1
    
print(store_rev_str)
    
    