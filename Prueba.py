# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:40:20 2022

@author: JRB23
"""

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Opcion 1 Suma de 2 números")
    print ("2. Opcion 2")
    print ("3. Opcion 3")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1 Suma de 2 números")
        n1=float(input("Intro número uno: "))
        n2=float(input("Intro numero dos: "))
        suma=n1+n2

        print("La suma es: ",suma)
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
    