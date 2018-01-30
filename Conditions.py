#Conditions Code
#Making Calculator

num1 = input("Enter the First no:")
print(num1)

operation = input("Enter the operation you want to perform:")
print(operation)

num2 = input("Enter the second number:")
print(num2)

if (operation == '+'):
    print(int(num1)+int(num2))

elif (operation == '-'):
    print(int(num1)-int(num2))

elif (operation=='*'):
    print (int(num1)*int(num2))

elif (operation=='/'):
    print (int(num1)/(num2))

else:
    print("You have entered wrong values")







