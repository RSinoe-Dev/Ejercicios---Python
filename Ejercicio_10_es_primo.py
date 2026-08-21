def es_primo(num):
    
    if num < 2: 
        return False
    
    divisor = 2

    while divisor < num:
        if num % divisor == 0:
             return False

        divisor = divisor + 1
    
    return True

print(es_primo(2))
print(es_primo(3))
print(es_primo(4))
print(es_primo(7))
print(es_primo(10))
print(es_primo(13))
print(es_primo(1))
