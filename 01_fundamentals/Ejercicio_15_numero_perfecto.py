def es_perfecto(num):

    suma = 0 
    divisor = 1

    while divisor < num:
        
        if num % divisor == 0:
            suma = suma + divisor
        
        divisor = divisor + 1
    
    return suma == num

print(es_perfecto(6))
print(es_perfecto(10))
print(es_perfecto(28))
print(es_perfecto(12))
print(es_perfecto(496))
