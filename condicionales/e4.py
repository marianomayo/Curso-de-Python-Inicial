sueldo = int(input("Ingrese el sueldo de la persona: "))

cabecera = "El sueldo ingresado es {0}"
print(cabecera.format(sueldo))
if sueldo > 3000:
    print("Esta persona debe pagar inpuesto")
if sueldo < 3000:
    print("La persona no paga inpuesto")

if sueldo > 6000 and sueldo<10000:
    print("El usuario tiene que pagar una bonificacion de 1000 euros")
if sueldo == 20000 or sueldo == 30000:
    print("El usuario paga un 10 porciento de su sueldo")