#  Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

str = input("Enter your string")
length = len(str)
save = ""
for i in range(length): 
    char = str[i]
    for i in range(length):
        char_2 = str[i + 1]
        if char !=char_2:
            save = char
            break