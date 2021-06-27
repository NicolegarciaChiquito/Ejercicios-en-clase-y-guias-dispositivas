<<<<<<< Updated upstream
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

class ciclo:
    
    def __init__(self,numero=5):
        self.numero=numero
        self.numero2=0
    
    def usoWhile(self):
        # ciclo repetitivo que se ejecuta mientras la condicion se cumple(verdadero),
        #es decir solo por falso
        car = input("Ingrese vocal: ")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("Ingrese vocal: ").lower()
        print("Felicitación su vocal es: {}".format(car))
            
ciclo1 = ciclo()
ciclo1.usoWhile()
=======
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

class ciclo:
    
    def __init__(self,numero=5):
        self.numero=numero
        self.numero2=0
    
    def usoWhile(self):
        # ciclo repetitivo que se ejecuta mientras la condicion se cumple(verdadero),
        #es decir solo por falso
        car = input("Ingrese vocal: ")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("Ingrese vocal: ").lower()
        print("Felicitación su vocal es: {}".format(car))
            
ciclo1 = ciclo()
ciclo1.usoWhile()
>>>>>>> Stashed changes
print("fin de uso ciclo")     