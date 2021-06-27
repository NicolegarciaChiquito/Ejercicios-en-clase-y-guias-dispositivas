<<<<<<< Updated upstream
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

#Funciones sin retorno
def vocales(frase):
     for car in frase:
         if car in('a','e','i','o','u'):
             print(car)
#Llamada a funcion             
oracion = input('Ingrese oracion: ')
vocales(oracion.lower())

print("=======================")

# llamada a funcion
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
=======
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

#Funciones sin retorno
def vocales(frase):
     for car in frase:
         if car in('a','e','i','o','u'):
             print(car)
#Llamada a funcion             
oracion = input('Ingrese oracion: ')
vocales(oracion.lower())

print("=======================")

# llamada a funcion
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
>>>>>>> Stashed changes
print('Promedio: {} = {}'.format(listanotas, prom))