Marks = int(input("Enter Marks: "))

if(Marks>=0)and(Marks<=100):
    if(Marks>=0) and (Marks<=39):
        print("Fail")
    elif(Marks>=40) and (Marks<=59):
        print("Third Class")
    elif(Marks>=60) and (Marks<=79):
        print("Second Class")
    elif(Marks>=80) and (Marks<=100):
        print("First Class")
else:
    print("Invalid Marks")
