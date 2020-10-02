#crear ciclo for que permita ingresar para n numero, donde n es un numero ingresado x teclado
#Calcular y mostrar: cantidad de numeros pares y cantidad de numeros impares

veces=int(input("Cuantos números ingresa?: "))
par=0
impar=0
for x in range(veces):
    nume=int(input("Ingrese un número: "))
    if (nume%2==0):
        par=par+1
    elif(nume%2!=0):
        impar=impar+1

print("La cantidad de números pares es: " + str(par))
print("La cantidad de números impares es: " + str(impar))