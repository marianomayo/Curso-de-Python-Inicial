def cargar_datos():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista

def verificar_mayor(lista):
    mayor = lista[0]
    for x in range(1, 5):
        if lista[x] > mayor:
            mayor = lista[x]
    print("El mayor de la lista es: ", mayor)

def verificar_suma(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    print("Suma de todos sus elementos es: ", suma)
