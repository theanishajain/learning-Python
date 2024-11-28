from array import *;
a1 = array('i',[3,5,6])
#PRINTING with for loop
for x in a1:
    print(x)
#printing with the help of range
for i in range(3):
    print(a1[i],end=" ")
    # print()
#running with the help of while loop
i = 0
print()
while i<len(a1):
    print(a1[i],end=" ")
    i=i+1#i+=1
