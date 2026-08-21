def factorial(num):
    if num == 0:
        return 1
    
    resultado = 1
    
    while num != 1:
        resultado = resultado * num
        num = num - 1 
    return resultado

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
