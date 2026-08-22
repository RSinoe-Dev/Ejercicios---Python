def mcd(a, b):

    while b != 0:

        nuevo = a % b
        a = b 
        b = nuevo

    return a
    
print(mcd(12, 8))
print(mcd(15, 10))
print(mcd(20, 8))
print(mcd(7, 3))
print(mcd(48, 18))
