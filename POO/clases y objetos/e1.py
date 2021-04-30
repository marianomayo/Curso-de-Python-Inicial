class alumno:

    def declarar(self, nombre, dato):
        self.nombre = nombre
        self.puntuacion = dato

    def visualizar(self):
        print("El nombre es: ",self.nombre)
        print("La puntuacion es: ", self.puntuacion)

    def estadisticas(self):
        if self.puntuacion<=4:
            print("Insuficiente")
        elif self.puntuacion>=5:
            print("Notable")
        elif self.puntuacion>=8:
            print("Sobresaliente")
        else: 
            print("Libre")



############Bloque principal##########

alumno1 = alumno()
alumno1.declarar("mariano mayo", 8)
alumno1.visualizar()
alumno1.estadisticas()


alumno1 = alumno()
alumno1.declarar("torres juan manuel", 4)
alumno1.visualizar()
alumno1.estadisticas()