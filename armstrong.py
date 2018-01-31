

num = int(input("Enter the number to check"))
print(num)
sum=0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp//=10

if sum==num:
    print(num,"is armstrong number ")
else:
    print("It is not")