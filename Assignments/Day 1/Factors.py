number = int(input("Enter Number: "))
i=1;
count=0;
sum=0;
while i<=number:
    if(number%i==0):
        print("Factor: ",i)
        sum=sum+i
        count=count+1
    i=i+1
else:
    print("Sum of Factors: ",sum)
    print("Number of Factors: ",count)
