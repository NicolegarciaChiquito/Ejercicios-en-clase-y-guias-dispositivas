<<<<<<< Updated upstream
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

""" num =20
nombre= "ana"
print(num,type(num))
print(nombre,type(nombre))
def mensaje(msg):
    print(msg)   
    
mensaje("Mi primer programa")
mensaje("Mi segundo programa") """

class sintaxis:
    instancia=0
     #__init__ Metodo constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
     #e iniciar los atributos de la clase. self es un objetivo que representa la clase creada
    def __init__(self ,dato="llamando al constructor1"):
        self.frase=dato #atributo de instancia
        sintaxis.instancia = sintaxis.instancia+1
    
    def usoVariables(self):
        edad, _peso=23, 64.5
        nombres = 'Nicole Garcia'
        Tipo_sexo = 'F'
        civil = True
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario=('ngarciac','146','ngarcia@gmail.com')
        # print(usuario[2],nombres[7])
        # #usuario[3] = "Guayaquil"
        # #lista = [] colecciones mutables
        materias=[]
        materias=['Programación Web','PHP','POO']
        aux=materias[1]
        materias[1]="python"
        materias.append("Go")
        #print(materias,aux, materias[1])
        
        # #diccionario = {} colecciones de objetos clave:valor tipo json
        docente={}
        docente = {'nombres':'Nicole','edad':23,'activo':True}
        edad=docente['edad']
        docente['edad']=24
        docente['carrera']='IS'
        # print(docente,edad,docente['edad'])
        # print(usuario,usuario[0], usuario[0:2],usuario[-1])
        # print(nombres,nombres[0], nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:3], materias[::-1],materias[-2:])
        # #presentacion con format
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres,edad))
# print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))        
ejer1=sintaxis() #instancia la clase sintaxis y crea el objeto ejer1(copia de la clase)
# print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
# ejer2=sintaxis("instancia2")
# print(ejer1.frase)
# print("sintaxis de ejer2 es: {}".format(sintaxis.instancia))
# print("sintaxis nuevamente ejer1 : {}".format(sintaxis.instancia))
# print(ejer2.frase)
=======
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

""" num =20
nombre= "ana"
print(num,type(num))
print(nombre,type(nombre))
def mensaje(msg):
    print(msg)   
    
mensaje("Mi primer programa")
mensaje("Mi segundo programa") """

class sintaxis:
    instancia=0
     #__init__ Metodo constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
     #e iniciar los atributos de la clase. self es un objetivo que representa la clase creada
    def __init__(self ,dato="llamando al constructor1"):
        self.frase=dato #atributo de instancia
        sintaxis.instancia = sintaxis.instancia+1
    
    def usoVariables(self):
        edad, _peso=23, 64.5
        nombres = 'Nicole Garcia'
        Tipo_sexo = 'F'
        civil = True
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario=('ngarciac','146','ngarcia@gmail.com')
        # print(usuario[2],nombres[7])
        # #usuario[3] = "Guayaquil"
        # #lista = [] colecciones mutables
        materias=[]
        materias=['Programación Web','PHP','POO']
        aux=materias[1]
        materias[1]="python"
        materias.append("Go")
        #print(materias,aux, materias[1])
        
        # #diccionario = {} colecciones de objetos clave:valor tipo json
        docente={}
        docente = {'nombres':'Nicole','edad':23,'activo':True}
        edad=docente['edad']
        docente['edad']=24
        docente['carrera']='IS'
        # print(docente,edad,docente['edad'])
        # print(usuario,usuario[0], usuario[0:2],usuario[-1])
        # print(nombres,nombres[0], nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:3], materias[::-1],materias[-2:])
        # #presentacion con format
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres,edad))
# print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))        
ejer1=sintaxis() #instancia la clase sintaxis y crea el objeto ejer1(copia de la clase)
# print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
# ejer2=sintaxis("instancia2")
# print(ejer1.frase)
# print("sintaxis de ejer2 es: {}".format(sintaxis.instancia))
# print("sintaxis nuevamente ejer1 : {}".format(sintaxis.instancia))
# print(ejer2.frase)
>>>>>>> Stashed changes
ejer1.usoVariables()