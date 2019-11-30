number = int(input("Enter Number: "))
i=2;
while i<= (number/2):
    if(number%i==0):
        print("Not Prime")
        break
    i=i+1
else:
    print(' Prime')
