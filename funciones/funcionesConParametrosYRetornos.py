def retorno_superficie(lado):
    sup = lado*lado
    return sup

va = int(input("introduce el valor del cuadrado: "))

superficie = retorno_superficie(va)

print("El algoritmo del cuadrado es: "+ str(superficie))