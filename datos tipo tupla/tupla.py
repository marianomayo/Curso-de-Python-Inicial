def cargarFecha():
    dd = int(input("Ingrese un dia"))
    mm = int(input("Ingrese un mes"))
    yy = int(input("Ingrese un año"))
    if mm == 1:
       mm = "enero"
    elif mm == 2:
       mm = "febrero"
    elif mm == 3:
        mm = "marzo"
    elif mm == 4:
        mm = "abril"
    elif mm == 5:
        mm = "mayo"
    elif mm == 6:
        mm = "junio"
    elif mm == 7:
        mm = "julio"
    elif mm == 8:
        mm = "agosto"
    elif mm == 9:
        mm = "septiembre"
    elif mm == 10:
        mm = "octubre"
    elif mm == 11:
        mm = "noviembre"
    elif mm == 12:
        mm = "diciembre"
    tupla = (dd, mm, yy)
    return tupla


def imprimir_fecha(fecha):         
    print(fecha[0], fecha[1], fecha[2], sep="/")


fecha = cargarFecha()
imprimir_fecha(fecha)