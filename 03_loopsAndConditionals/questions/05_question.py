# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. 
# (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

leap_year = int(input("Enter the year"))

if leap_year % 4==0:
    if leap_year % 100 != 0 or leap_year %  400 == 0:
        print("The year is leap year")
    else: 
        print("The year is not a leap year")
