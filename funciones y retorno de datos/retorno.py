def retornar ( d1, d2):
    if d1> d2:
        m=d1
    else:
        m=d2
    return m

d1= 20
d2 = 15

valor = retornar(d1, d2)
print("El valor retornado es ", valor)