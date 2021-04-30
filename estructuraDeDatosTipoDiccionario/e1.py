def cargar():
    diccionario={}
    continua = "s"
    while continua == "s":
        caste = input("Ingrese palabra en castellano: ")
        ing = input("Ingrese palabra en ingles: ")
        diccionario[caste] = ing
        continua = input("Quiere cargar otra palabra: [s/n]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])


def consultar_palabra(diccionario):
    pal = input("Ingrese lapalabra en castellano a consultar: ")
    if pal in diccionario:
        print("En ingles significa: ",diccionario[pal])


diccionario = cargar()
imprimir(diccionario)
consultar_palabra(diccionario)