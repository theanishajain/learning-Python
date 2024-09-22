# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

color = input("Enter the color of your fruit.")
if color == "Green":
    print("Your fruit is Unripe", color )
elif color == "Yellow":
    print("Your fruit is Ripe", color)
else :
    print("Your fruit is Overripe", color)