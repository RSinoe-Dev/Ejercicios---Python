def contar_digitos(num):

    if num == 0:
        return 1

    contar = 0

    while num != 0:
        num = num // 10
        contar += 1
    return contar

print(contar_digitos(0))
print(contar_digitos(5))
print(contar_digitos(42))
print(contar_digitos(123))
print(contar_digitos(98765))
