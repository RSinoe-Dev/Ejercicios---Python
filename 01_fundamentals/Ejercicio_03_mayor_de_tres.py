def mayor_de_tres(a, b , c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b 
    else:
        return c

print(mayor_de_tres(10, 5, 20))
print(mayor_de_tres(3, 15, 7))
print(mayor_de_tres(4, 6, 20))
print(mayor_de_tres(7, 7, 3))
print(mayor_de_tres(-2, -8, -5))
