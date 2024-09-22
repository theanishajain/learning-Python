class Rectangle:
    def set_dimensions(self,width,height):
        self.width = width
        self.height = height
     
    def calculatesArea(self):
         return self.width*self.height
         
         
    def perimeter(self):
         return 2*(self.width+self.height)
     
     
# print(input("Enter anything"))
# width = int(input("Enter the width"))
# height = int(input("Enter the height"))

rectangle1 = Rectangle()
rectangle1.set_dimensions(2,4)
print(rectangle1.perimeter())
