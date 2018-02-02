#Directly

x=3
y=4

x,y=y,x

print(x,y)

#Without using temporary variable.

a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)

