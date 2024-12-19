n = 123451
d = 1
count = 0
while(n>0):
 digit = n%10
 if digit == d:
     count += 1
 n = n//n

print(count)