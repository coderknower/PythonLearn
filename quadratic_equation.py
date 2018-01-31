# Solving the quadratic equations. Example: ax**2+bx+c=0
# Solutions can be find using -b+sqrt(b**2-4ac)/ 2a and -b-sqrt(b**2-4ac)/ 2a

import cmath
a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))

d = b**2 - 4*a*c
print(d)

sol1= (-b-cmath.sqrt(d))/2*a
sol2= (-b+cmath.sqrt(d))/2*a

print ("The solution is ", sol1,sol2)

