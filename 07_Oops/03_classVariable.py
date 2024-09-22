# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.
class Student:
    total = 0 
    
    def __init__(self, name):
          Student.total += 1
          self.name = name
        #   total_times_created += 1
        
        
s1 = Student("John")
print(s1.name)
print(Student.total)