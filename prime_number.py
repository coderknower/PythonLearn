


num = int(input("Enter the Number:"))
print(num)

for num in range(1,num):

    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print("Number is not prime and is divisible by", i)
                break

        else:
            print("Number is prime")

