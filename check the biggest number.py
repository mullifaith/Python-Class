a = int(input("enter value of a"))
b = int(input("enter value of b"))
c = int(input("enter value of c"))
if a > b:
    if a > c:
        print(f"{a} is bigger than {b} and {c}")
    else:
        print(f" {c} is bigger than {a} and {b}")
elif b > c:
    print(f" {b} is bigger than {a} and {c}")
else:
    print(f" {c} is bigger than {a} and {b}")
