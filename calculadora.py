#!/usr/bin/python
#Agustin Gonzalez C.I: 22.998.579
import math

def cuadrado(x):
    return x**2

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplica(x,y):
    return x*y

def divide(x,y):
    if y > 0:
        return x/y
    else:
        print 'No es divisible'

def factorial(x):
    x=math.factorial(x)
    return x

def raiz(x):
   r=math.sqrt(x)
   return r


def main():
    print "     Calculadora"
    print "-------------------------------"
    resp = "s"
    while resp=="s" or resp=="S":
            x=input("Ingrese un numero: ")
            y=input("Ingrese otro numero: ")
            print "-------------------------------"
            print "   Operaciones"
            print "-------------------------------"
            print "1. Sumar"
            print "2. Restar"
            print "3. Multiplicar"
            print "4. Dividir"
            print "5. Factorial de ambos numeros"
            print "6. Raiz de ambos numeros"
            print "-------------------------------"
            opc= input("Selecion de operacion: ")

            if (opc==1):
                print "Resultado: ",suma(x,y)
            elif(opc==2):
                print "Resultado: ",resta(x,y)
            elif(opc==3):
                print "Resultado: ",multiplica(x,y)
            elif(opc==4):
                print "Resultado: ",divide(x,y)
            elif(opc==5):
                print "Factorial del 1er numero: ",factorial(x)
                print "Factorial del 2do numero: ",factorial(y)
            elif(opc==6):
                print "Raiz del 1er numero: ",raiz(x)
                print "Raiz del 2do numero: ",raiz(y)

            print "---------------------------"
            resp = raw_input("Segir calculando? S/N: /n")




main()
