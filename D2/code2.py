mark = float(input("Enter mark :"))

if( mark >= 90):
    print("Grade is : A")
elif(mark < 90 and mark >= 80):
    print("Grade is : B")
elif(mark < 80 and mark >= 70):
    print("Grade is : C")
else:
    print("Grade is : D")