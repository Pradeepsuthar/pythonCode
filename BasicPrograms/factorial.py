# factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
    
n = 5    
print("factorial of %d :"%n,fact(n))