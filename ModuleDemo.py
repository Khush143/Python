import UDF

while True:

    print("*******************************")
    print("1. OddEven")
    print("2. MexOfTwo")
    print("3. MexOfThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*******************************")


    choice=input("Enter Your Choice : ")
    print("*******************************")

    if choice==1:
        a=int(input("Enter Value :"))
        UDF.OddEven(a)
        print("***************************")

    
    elif choice==2:
         a=int(input("Enter Value :"))
         b=int(input("Enter Value :"))
         UDF.MaxOfTwo(a,b)
         print("***************************")

    elif choice==2:
         a=int(input("Enter Value :"))
         b=int(input("Enter Value :"))
         c=int(input("Enter Value :"))
         UDF.MaxOfThree(a,b,c)
         print("***************************")

    elif choice==4:
        a=int(input("Enter Value :"))
        UDF.Fibonacci(a)
        print("***************************")

    elif choice==5:
        a=int(input("Enter Value :"))
        UDF.prime(a)
        print("***************************")

    else:
        break