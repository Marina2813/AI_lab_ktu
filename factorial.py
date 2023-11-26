def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        i = i+1
    return fact

n = int(input("Enter a number: "))
fact = factorial(n)
print(f'The factorial of the given number  is {fact}')