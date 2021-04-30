class operacion:

    def __init__(self):
        self.valor1=0
        self.valor2=0


    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)    

    def restar(self):
        resta = self.valor1 - self.valor2
        print("La resta es: ", resta)
    
    def multiplicacion(self):
        multiplicar = self.valor1 * self.valor2
        print("La multiplicacion es: ", multiplicar)

    def division(self):
        division = self.valor1 / self.valor2
        print("La division es: ", division)

    def intro_valores(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))

    def main(self):
        self.sumar()
        self.restar()
        self.multiplicacion()
        self.division()


#Bloque principal

operacion1=operacion()
operacion1.intro_valores()
operacion1.main()