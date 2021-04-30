nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2:  "))
nota3 = int(input("Ingrese nota 3:  "))
insuficiente = "insuficiente"
cabecera = "Las notas ingresadas son nota1: {0}, nota2: {1}, nota3: {2}  "
print(cabecera.format(nota1, nota2, nota3))

media = (nota1+nota2+nota3) / 3

if media == 9 or media == 10:
    print("El alumno es sobresaliente")
elif media == 5:
    print("Suficiente")
elif media == 6:
    print("bien")
elif media == 7 or media == 8:
    print("regular/bien")
else:
    print(insuficiente)
    