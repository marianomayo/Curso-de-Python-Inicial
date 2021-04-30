archivo = open("archivo.txc", "w+")

contenido = archivo.read()   #lee el archivo
final_de_archivo = archivo.tell()  #retorna la posicion

archivo.write('Nueva linea')   #escribimos dentro del archivo, le mandamos un string
archivo.seek(final_de_archivo)        #mover el puntero a write indicado
nuevo_contenido = archivo.read()  #almacenamos la variable

archivo.close()     #cerramos archivo

print(nuevo_contenido)  #visualizamos archivo

#Nueva linea