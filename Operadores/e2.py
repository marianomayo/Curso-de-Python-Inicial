print("datos de la primera persona")

##input me sirve para el ingreso del valor de una variable
## cuando quiero cargar un numero de forma obligatoria pongo anteriormente al input el int
nombre1 = input("Ingrese nombre de producto:")
precio1 = int(input("Ingrese Precio:"))
nombre2 = input("Ingrese nombre de producto:")
precio2 = int(input("Ingrese Precio:"))

##LAS CONSTANTES SE PONEN CON LETRA MAYUSCULA
BONIFICACION = 20

precio_compra_total = precio1 * precio2

comparar = precio1 > precio2
logico = (precio1 < precio2 and precio1 == precio2)

##contatenaciones de texto

cabecera = "resultado del producto {0}. y del producto .{1}.:"
##contatenamos las cadenas de texto y les damos los valores con format
print(cabecera.format(nombre1,nombre2))

print("El precio del primer valor es mayor que el segundo")
print(comparar)
## concatenar se puede hacer de esta manera con el sing + y en la variable la propiedad srt
print("la suma de los productos es: " + str(precio_compra_total))
print("precio1 < precio2 and precio1 == precio2")
print(logico)

precio_compra_total =+ BONIFICACION
print("al precio total le incrementamos su valor que tiene la constante"+ str(precio_compra_total))