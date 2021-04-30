sueldo1 = int(input("Ingrese el primer sueldo: "))
sueldo2 = int(input("Ingrese el segundo sueldo sueldo: "))

cabecera = "Los sueldos ingresados son {0}.   y    .{1}.:"
print(cabecera.format(sueldo1,sueldo2))

if sueldo1 > sueldo2:
    print("El sueldo 1: "+str(sueldo1) + " Es mayor al sueldo 2 que es: "+ str(sueldo2))

if sueldo1<sueldo2:
    print("El sueldo 2: "+str(sueldo2)+" es mayor al sueldo 1 que es : "+ str(sueldo1))