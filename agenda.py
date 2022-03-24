#Menú de la agenda
def menu():
    print ("|-----------------------------------|")
    print ("|   AGENDA ADRIAN LLAMAS CRUZ       |")
    print ("|-----------------------------------|")
    print ("|     1. Añadir o modificar         |")
    print ("|     2. Buscar                     |")
    print ("|     3. Borrar                     |")
    print ("|     4. Listar                     |")
    print ("|     5. Salir                      |")
    print ("|-----------------------------------|")
    

#Función añadir o modificar.
#Se pide un nombre y un número.
#Se comprueba si está en la agenda, si es así se le da la opción a modificarlo.
#Sino está en la agenda se le pide un número de teléfono y un nombre para añadir el nuevo contacto a la agenda.
def añadirModificarAllamas (nombre,agenda):
    if nombre in agenda:
        print(nombre," ya existe su número de teléfono es ",agenda[nombre])
        opcion = input("Pulsa 's' si quieres modificarlo. Otra tecla para continuar.")
        if opcion == "s":
            numero = input("Dame el nuevo número de teléfono:")
            agenda[nombre]=numero
    else:
        numero = int(input("Dame el número de teléfono:"))
        agenda[nombre]=numero
            
#Esta programa fue creado el martes 8 de marzo de 2022
#Este es el código de la búsqueda de Andrés Serrano Rodríguez, sirve para realizar búsquedas en la agenda a partir de nombres de usuarios.
def buscar_ASerrano(nombre, agenda):
        for cadena,numero in agenda.items():
                if cadena.startswith(nombre):
                        print("El número de teléfono de %s es el %s " % (nombre,agenda[cadena])) 

###Parte de agenda Tomás Cabello Fernández,10/03/2022###
###Función borrar###
###Está función te pide un nombre, si le das un contacto existente,###
###te responde pidiendote el pulsado de la tecla s para confirmar el borrado###
###Si no existe el contacto simplemente el programa responde diciendo que no existe.###  
def borrar_Tcabello(nombre, agenda):
    if nombre in agenda:
        opcion = input("Pulsa 's' si quieres borrarlo. Otra tecla para continuar.")
        if opcion == "s":
            del agenda[nombre]
    else:
        print("No existe el contacto.")

        

#Es una función que hace la función de listar el nombre y número de la agenda
#AUTOR: Emilio Pastor 
#FECHA: 4/03/2022
#HORA: 14:00
def listar_EPastor(agenda):
    for nombre, numero in agenda.items(): #Significa que nos da la información si está el nombre y número en la agenda
            print("--------------")
            print(nombre)#Nos da el nombre
            print("|| || || ||")
            print("\/ \/ \/ \/")
            print(numero)#Nos da el número del mismo
            print("--------------")

            
#################################################################################################################################################################

agenda = {}
menu()
opcion = int(input("Selecciona una opción: "))
while (opcion <=0 or opcion >=6):
    print ("Numero incorrecto")

while (opcion >=0 or opcion <=6):
    if (opcion ==1):
        nombre = input ("Escribe el nombre del contacto: ")
        añadirModificarAllamas (nombre,agenda)

    elif (opcion==2):
        nombre = input("Nombre del contacto: ")
        buscar_ASerrano(nombre, agenda)

    elif (opcion==3):
        nombre = input ("Nombre del contacto que quieres borrar: ")
        borrar_Tcabello(nombre, agenda)

    elif (opcion==4):
        listar_EPastor(agenda)

    elif (opcion==5):
        exit()
    menu()
    opcion = int(input("Seleciona una opción: "))
