#define our own function
#def function_name ():

def greetings():
    print("Hi, Students")

greetings()



def greeting(fname, lname):
    print(f"Hi {fname}, {lname}")

greeting(fname="Faith", lname="Mulli")



def oddoreven(num):
    if num % 2 == 0:
        result = "even"
    else:
        result = "odd"

        print(result)
        
oddoreven(556565)
