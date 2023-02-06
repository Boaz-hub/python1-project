#program to find the largest for 3 numbers
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num1>num2 and num1>num3:
    print("Num1 is the largest")
elif num2>num1 and num2>num3:
    print("Num2 is the largest")
else:
    print("Num3 is the largest")
