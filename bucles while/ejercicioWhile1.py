x = 1
suma = 0

while x <= 5:
    valor=int(input("ingrese un valor:"))
    suma = suma+valor
    x= x+1

promedio = suma/10

print("La suma de los valores es " +str(suma))
print("El promedio es: "+ str(promedio))