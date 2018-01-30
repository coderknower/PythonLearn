

def area1(x,y):
    return 0.5*float(x)*float(y)

def area2(a,b,c):
    s= (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
1


choice = input("What are the dimensions of the triangle which you have:\n"
               "1.If you have height and base\n"
               "2.If you have all sides\n")
print(choice)

if (choice=='1'):
    base= input("Enter the base of triangle:")
    print(base)
    height= input("Enter the height of triangle:")
    print(height)
    print("The area of triangle is ",area1(base,height))

elif (choice=='2'):
    s1=int(input("Enter side1"))
    print(s1)
    s2 = int(input("Enter side2"))
    print(s2)
    s3 = int(input("Enter side3"))
    print(s3)
    print("The area of triangle is ",area2(s1,s2,s3))

else:
    print("You have entered wrong values")
