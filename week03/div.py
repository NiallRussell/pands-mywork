x = int(input("Enter first number:"))
y = int(input("Enter the number you want to divide by:"))
answer = int(x//y)
remainder = x%y 
if remainder == 0:
    print("{} divided by {} is {}".format(x,y,answer))
else:
    print("{} divided by {} is {} with remainder {}".format(x,y,answer,remainder))
