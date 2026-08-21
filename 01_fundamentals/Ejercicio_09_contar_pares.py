def contar_pares(num):

    contar = 0 
    numero = 1

    while numero <= num: 

        if numero % 2 == 0:
            contar = contar + 1
        
        numero = numero + 1

    return contar

print(contar_pares(10))
print(contar_pares(7))
print(contar_pares(20))
