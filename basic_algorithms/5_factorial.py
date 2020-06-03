def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

n = int(input("Write a number : "))

factorial_n = factorial(n);

print(f"The factorial of {n} is {factorial_n}")