while True:
    def root(x):
       return x**0.5

    def cuberoot(x):
        return x**0.33333333333


    num1 = int(input("Enter the number"))
    print(num1)

    operation = input("Enter the operation you want to perform:"
                      "1 for root"
                      "2 for cube-root"
                      )
    print(operation)



    if (operation == '1'):
        print(root(num1))

    elif (operation == '2'):
        print(cuberoot(num1))

    else:
        print("You have entered wrong values")

    def root(x):
       return x**0.5

    def cuberoot(x):
        return x**0.33333333333

    loop= input("Do you want to try again(y for yes and n for no):")
    print(loop)
    if (loop =='y'or 'Y'):
        continue
    else:
        break
