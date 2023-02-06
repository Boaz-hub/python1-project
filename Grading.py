#write a program to create grading system
sub1= int(input("Enter marks of sub1: "))
sub2= int(input("Enter marks of sub2: "))
sub3= int(input("Enter marks of sub3: "))
sum=(sub1+sub2+sub3)
avg=(sub1+sub2+sub3)/3
if avg >=70:
    print("A")
elif avg>=60 and avg<=69:
    print("B")
elif avg>=50 and avg<=59:
    print("C")
elif avg>=40 and avg<=49:
    print("D")
else:
    print("Fail")


