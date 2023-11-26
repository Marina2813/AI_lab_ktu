def fibonacci(n):
    a,b=1,1
    for i in range(n):
        print(a,end=" ")
        temp = a
        a=b
        b=temp+b

n= int(input("Enter a number: "))
fibonacci(n)
