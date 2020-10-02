#crear menu con 3 opciones: 1. Numeros, 2. Personas, 3. Finalizar

import os 
def Numeros():
    #ingresar n números donde n es un número ingresado por el usuario.
    #mostrar la cantidad de números positivos, cantidad de números negativos y cantidad
    #de números iguales a cero
    n=int(input("ingrese cuantos numeros necesita: "))
    a=0
    b=0
    c=0
    d=0
    for i in range(n):
    
        a=int(input("ingrese: "))
        if(a>0):
       	    b=b+1
        elif(a==0):
       	    c=c+1
        elif(a<0):
            d=d+1
    print("positivos: "+ str(b)+ " negativos: "+ str(d)+ "cero: "+ str(c))
    pausa=input("Presione una tecla para continuar: ")

def Personas():
    #ingresar nombre y edad para n personas. N es un numero ingresado por teclado.
    #mostrar: promedio de todas las edades ingresadas
    n=int(input("ingrese numero de personas "))
    a=0
    sum=0
    for i in range(n):
        nom=input("ingrese nombre de la persona")
        a=int(input("ingrese edad de la persona: "))
        sum=sum+a

    print("promedio de las edades: " + (sum/n)
    pausa=input("Presione una tecla para continuar ")

seguir=True
while(seguir):
    os.system('cls')
    print(" ---- Menú Principal ----")
    print("1. Números")
    print("2. Personas")
    print("3. Finalizar")
    op=int(input("Digite opción 1,2,3: "))
    if (op==1):
        Numeros()       #invocamos a un def
    if (op==2):
        Personas()      #invocamos a un def
    if (op==3):
        print("Programa finalizado")
        seguir=False
        break