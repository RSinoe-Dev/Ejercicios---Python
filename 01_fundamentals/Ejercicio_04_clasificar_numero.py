def clasificar_num(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

print(clasificar_num(10))
print(clasificar_num(-5))
print(clasificar_num(0))
