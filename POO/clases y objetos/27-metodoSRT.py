class Familia:

    def __init__(self, padre, madre, hijos=[]):
        self.padre=padre
        self.madre = madre
        self.hijos=hijos
    
    def __str__(self):
        cadena = self.padre+","+self.madre
        for hijo in self.hijos:
            cadena = cadena+","+hijo
        print("___________")
        return cadena



##bloque principal

familai1= Familia("Pablo", "Ana", ["Pepe", "julio"])
familai2= Familia("jose", "Nancy", ["Mariano"])
familai3= Familia("david", "Andrea", ["Nicolas", "Lautaro"])

print(familai1)
print(familai2)
print(familai3)