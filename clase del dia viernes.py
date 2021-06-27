<<<<<<< Updated upstream
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1
#Clases del dia Viernes 18/06/2021
class For:
    def usoFor(self):

        listasNotas=[(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listasNotas:
            print(notas)
            acump=0
            contp=0
            for nota in notas:
                acump +=nota
                acum=acum+nota
                cont=cont+1
            print(acump/len(notas))
        print(acum/cont)
bucle = For()
=======
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1
#Clases del dia Viernes 18/06/2021
class For:
    def usoFor(self):

        listasNotas=[(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listasNotas:
            print(notas)
            acump=0
            contp=0
            for nota in notas:
                acump +=nota
                acum=acum+nota
                cont=cont+1
            print(acump/len(notas))
        print(acum/cont)
bucle = For()
>>>>>>> Stashed changes
bucle.usoFor()