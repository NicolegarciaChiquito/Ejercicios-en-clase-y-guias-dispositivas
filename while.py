<<<<<<< Updated upstream
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

#uso de while infinito 
s = 1
while True:
    print(s)
    break
# while validacion
vocal = input("Ingrese vocal:")
while vocal not in('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal = input("Igrese nuevamente una vocal:")
=======
#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1

#uso de while infinito 
s = 1
while True:
    print(s)
    break
# while validacion
vocal = input("Ingrese vocal:")
while vocal not in('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal = input("Igrese nuevamente una vocal:")
>>>>>>> Stashed changes
print('Su vocal o punto es: {}'.format(vocal))