


fibo=int(input("Enter the number of terms of fibonacci numbers in series you want:"))
print(fibo)


    n1= 0
    n2= 1
    count=0
    while count<fibo:
        nth= n1 + n2
        print(nth)
        n2 = n1
        n1 = nth

        count+=1
