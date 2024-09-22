# class Account:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#         self.amount = amount
        
#     def debit(self,amount):
#         self.balance -= amount
#         print(amount)
        
#     def credit(self,amount):
#         self.balance += amount
#         print(amount)
        
#     def balance(self):
#         return self.balance

# css multi line comments :  
class Student:
    def __init__(self, name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        
    def get_avg(self):
         add = 0 
         for i in self.marks:
             add = add + i
         return add/3
     
     
obj1 = Student("anisha",22,[23,55,66])
print(obj1.get_avg())
             
            
            
        