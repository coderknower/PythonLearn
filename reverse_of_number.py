

n = int(input("Enter the number:"))
print(n)

rev=0
while n>0:
    dig= n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)