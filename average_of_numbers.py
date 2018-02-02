

n=int(input("Total numbers whose average you want to find out:"))
print(n)
a=[]
for i in range(0,n):
     elem=int(input("Enter elements:"))
     a.append(elem)

     avg=sum(a)/n

print("The average is"+ avg)