def invertir_numero(num):
    resultado = 0

    while num != 0:
        digito = num % 10
        num = num // 10
        resultado = resultado * 10 + digito

    return resultado

print(invertir_numero(59))
print(invertir_numero(123))
print(invertir_numero(458))
print(invertir_numero(9001))
