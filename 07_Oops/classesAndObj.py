#classes names start with the capital letter
# Types of attributes
# 1.class attributes
# 2. instance attributes
 
class Student:
    # name = "Anisha"
    #default constructor
    college_name = "ABC College"
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, fullname, marks):  #without self code was not working 
        #passing argument or parameter into an object is mandatory
        # The self parameter is a reference to the current instance of the class and is used to acces the varibles
        # that belongs to that class
        # attributes : data or variables
        self.name = fullname
        self.marks= marks
        
    def get_marks(self):
        return self.marks
        
        print("Adding new girls in a database")
    # name = "Anisha"
    
s1 = Student('Aj', 44)
print(s1.name)
print(s1.marks)

s2 = Student('Anisha', 55)
print(s2.get_marks())



#Static Methods - Methods that don't use the self parameter[work at class level]
class Car:
    @staticmethod   #decorator
    def car_showroom():
            print("Welcome to our showroom")
            

car1 = Car()
print(Car.car_showroom())


# ABSTRACTION: hiding the implementation detail and showing only the essential part
# or features to the user

#ENCAPSULATION: wrapping data into single unit(object)


class account:
    def __init__(self, accNo, balance):
        self.accountNumber = accNo
        self.balance = balance
        
    def debit(self, amount):
        self.balance -= amount
        print(self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print(self.get_balance())
    def get_balance(self):
        return self.balance