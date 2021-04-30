def sumaDeValores(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma+lista[x]
    return suma

def valorMayor(lista):
    may = lista[0]
    for x in range(len(lista)):
        if lista[x] > may:
            may = lista[x]
        return may

def valorMenor(lista):
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] < men:
            men = lista[x]
        return men

datos=[458, 369, 859, 753, 1000, 5829, 789654, 63, 6548]
print("total de datos")
print(datos)
print("el valor de la suma del array es ", sumaDeValores(datos))
print("El numero mayor es ", valorMayor(datos))
print("el numero menor es: ", valorMenor(datos))