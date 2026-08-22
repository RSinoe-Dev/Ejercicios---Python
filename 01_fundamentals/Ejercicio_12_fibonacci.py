def fibonacci(n):

    a = 0
    b = 1

    if n == 0:
        return 0

    if n ==1:
        return 1
        
    while n != 1:

        siguiente = a + b
        a = b 
        b = siguiente
        n = n - 1
    
    return b

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(7))
