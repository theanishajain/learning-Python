# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

grade = int(input("Enter your numbers"))
if grade >= 90:
   print("A")
elif grade >= 80:
    print("B")
elif grade>= 70:
    print("C")
elif grade >= 60:
    print("D")
else: 
    print("F")