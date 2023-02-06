"""
Type if simple

1. if Semple

    if Condition:
        Statement
"""

a=int(input("Enter A :"))

if a>0:
    print("A is Positive number")   

"""
2. if/else

    if Condition:
        Statement

    else Condition:
        Statement
"""

a=int(input("Enter A :"))

if a%2==0:
    print("A is Even number")  
else:
    print("A is Odd number") 
'''
a=int(input("Enter A :"))
b=int(input("Enter B :"))

if a>b:
    print("A is Greater number")

else:
    print("B is Greater number")
'''

"""
3. Nested if/else

    if Condition:
        if Condition:
            Statement

        else Condition:
            Statement

    else Condition:
        Statement
"""

a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if a>b:
    if a>c:
        print("A is Greater number")
    else:
        print("C is Greater number")

elif b>c:
    print("B is Greater number")
else:
    print("C is Greater number")

"""
Ledder if/else
    if Condition:
        Statement
    
    elif Condition:
        Statement

    elif statement:
        Statement:

    else Condition:
        Statement
"""
rno=int(input("Enter Roll No :"))
sname=input("Enter Student Name :")
s1=int(input("Enterv Marks Of Subject 1 :"))
s2=int(input("Enterv Marks Of Subject 2 :"))
s3=int(input("Enterv Marks Of Subject 3 :"))

total=s1+s2+s3
per=total/3

print("Roll No :",rno)
print("Student Name :",sname)
print("Total :",total)
print("Percentage :",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=33:
    print("Pass")
else:
    print("Fail")