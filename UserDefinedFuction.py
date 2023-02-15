# function with no argument &bno return value.

def printline():
    print("*"*50)

printline()
print("Welcome To Defined Function In Python")
printline()

# function with argument but no return value.

def add(a,b):
    print("Addition : ",a+b)

printline()
x=int(input("Enter Value :"))
y=int(input("Enter Value :"))
add(10,20)
printline()
 
# function with argument & return value.
def sub(a,b):
    return a-b

printline()
x=int(input("Enter Value :"))
y=int(input("Enter Value :"))
print("Subtraction :",sub(x,y))
printline()