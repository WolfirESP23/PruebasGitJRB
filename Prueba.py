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
    print ("2. Opcion 2 Resta de 2 números")
    print ("3. Opcion 3 Multiplicación")
    print ("4. Opcion 4 División")
    print ("5. Opcion 4 Cuadrado")
    print ("6. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1 Suma de 2 números")
        n1=float(input("Intro número uno: "))
        n2=float(input("Intro numero dos: "))
        suma=n1+n2

        print("La suma es: ",suma)
    elif opcion == 2:
        print ("Opcion 2 Resta de 2 números")
        n1=float(input("Intro número uno: "))
        n2=float(input("Intro numero dos: "))
        resta=n1-n2

        print("La resta es: ",resta)
    elif opcion == 3:
        print("Opcion 3 Multiplicación")
        n1=float(input("Intro número uno: "))
        n2=float(input("Intro numero dos: "))
        mult=n1*n2

        print("La multiplicación es: ",mult)
    elif opcion == 4:
        print("Opcion 4 División")
        n1=float(input("Intro número uno: "))
        n2=float(input("Intro numero dos: "))
        div=n1*n2

        print("La división es: ",div)
    elif opcion == 5:
        print("Opcion 4 Cuadrado")
        n1=float(input("Intro número uno: "))
        cua=n1*n1

        print("La cuadrado es: ",cua)
    elif opcion == 6:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin del programa")
    