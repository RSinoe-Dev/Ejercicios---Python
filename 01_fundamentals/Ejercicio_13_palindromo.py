def es_palindromo(num):
    
    original = num 
    resultado = 0

    while num != 0:
        digito = num % 10
        num = num // 10
        resultado = resultado * 10 + digito
    
    if original == resultado:
        return True 
    else:
        return False
    
print(es_palindromo(121))
print(es_palindromo(123))
print(es_palindromo(1221))
print(es_palindromo(1234))
