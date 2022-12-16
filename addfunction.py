def addnumbers(n1, n2):
    sum = n1+n2
    print(sum)
addnumbers(6, 10)

def sq(num):
    result = num * num
    return result
s = sq(10)
print(s)

def square(num):
    return num * num
for i in [5,10,8,3]:
    result = square(i)
    print(result)

def area(l, w):
    sum = l*w
    return sum
a = area(8, 11)
print(a)



def increase(number, by):
    inc = number + by
    return inc
i = increase(number=100, by=30)
print(i)


def family(fname):
    return fname + " " + "Mulli"
for name in ["Faith","Jane","Joe"]:
    result =family(name)
    print(result)

