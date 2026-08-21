def suma_digitos(num):

    suma = 0

    while num != 0:
        digito = num % 10
        num = num // 10
        suma += digito   
    return suma

print(suma_digitos(123))
print(suma_digitos(458))
print(suma_digitos(9001))
