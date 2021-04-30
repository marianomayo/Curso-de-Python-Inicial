nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2:  "))
nota3 = int(input("Ingrese nota 3:  "))

cabecera = "Las notas ingresadas son nota1: {0}, nota2: {1}, nota3: {2}  "
print(cabecera.format(nota1, nota2, nota3))

promedio = (nota1+nota2+nota3) / 3

if promedio >=7:
    print("El alumno promociona")
else:
    if promedio>=4:
        print("El alumno aprueba")
    else:
        print("El alumno desaprueba")