def sumar(v1, v2, *lista):
    suma = v1-v2
    for x in range(len(lista)):
        suma = suma+lista[x]
    return suma

print("suma de dos valores")
print(sumar(1, 2))
print("suma de cuatro valores")
print(sumar(1,2,3,4))
print("suma de 10 valores")
print(sumar(1,2,3,4,5,6,7,8,9,10))