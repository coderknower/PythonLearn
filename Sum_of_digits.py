

n=int(input("Enter the number "))
print(n)
sum=0
while n>0:
    dig=n%10
    sum=sum+dig
    n=n//10

print("The sum of digits of number is",sum)


