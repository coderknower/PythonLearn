#Conditions Code
#Making Calculator and used while and if conditions along with loops

while True:

    num1 = input("Enter the First no:")
    print(num1)

    operation = input("Enter the operation you want to perform:\n "
                      " + \n "
                      " - \n  "
                      " * \n "
                      " / \n "
                      )
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


    loop= input("Do you want to try again(y for yes and n for no):")
    print(loop)
    if (loop =='y'or 'Y'):
        continue
    else:
        break






