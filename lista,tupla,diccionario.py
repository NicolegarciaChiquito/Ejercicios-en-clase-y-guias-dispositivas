#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1
# Guia dispositiva

# Tuplas – Listas - Diccionarios
usuario = ("Ngarcia", "146", "Nicolegarcia-146@hotmail.com")
materias = ["Estructura_de_datos", "ecuaciones", "modelamiento_de_Software"]
docente = {"nombre":"Nicole", "edad":23,"fac":"faci"}
print(usuario[0],materias[1],docente["nombre"])
print(usuario[0:2],docente.keys(),docente.values())
tupla,lista,diccionario=(),[],{}

materias.append("Estructura_de_datos")
docente["sexo"], docente["edad"]="Femenino", 23
print(materias,docente)
tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)
# Recorridos diccionario con items
for c, v in docente.items(): print(c,':',v)