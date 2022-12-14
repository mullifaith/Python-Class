print("Enter the Year")
y= int(input())
if y % 4==0 and y % 100 !=0:
    print(y, "is a leap year")
elif y % 400==0:
    print(y, "is a leap year")
else:
    print("it's not a leap year")
