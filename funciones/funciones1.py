def presentation():
    print("Programa para hacer operaciones aritmeticas")
    print("##################################")


def introducirDatos():
    global valor1
    global valor2
    valor1 = int(input("Ingrese el primer valor"))
    valor2 = int(input("Ingrese el segundo valor"))


def mostrarValoresIngresados():
    cabecera = "Los numeros ingresados son {0} y {1}"
    print(cabecera.format(valor1, valor2))

def suma():
    suma = valor1 + valor2
    print("La suma de "+str(valor1) +" + "+ str(valor2)+" es: "+str(suma))


def resta():
    resta = valor1 - valor2
    print("La resta de "+str(valor1)+ " - "+ str(valor2)+" es: "+str(resta))


def finalizar():
    print("GRACIAS X UTILIZAR ESTE PROGRAMA")

##
presentation()
introducirDatos()
mostrarValoresIngresados()
suma()
resta()
finalizar()