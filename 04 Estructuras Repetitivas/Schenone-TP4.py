# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un número entero: "))
contador = 0

while num > 1:
    num /= 10
    contador += 1

print("La cantidad de dígitos es:", contador)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
suma = 0

if numero1 < numero2:
    for i in range(numero1 + 1, numero2):
        suma += i
elif numero2 < numero1:
    for i in range(numero2 + 1, numero1):
        suma += i
else:
    suma = 0

print("La suma de los números entre", numero1, "y", numero2, " es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
num = int(input("Ingrese un numero entero para comenzar la suma (Ingrese 0 para salir): "))
while num != 0:
    suma += num
    num = int(input("Ingrese otro numero entero (Ingrese 0 para terminar): "))

print("La suma de los numeros ingresados es: ", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0, 9)
num = int(input("Adivina el número entre 0 y 9: "))
intentos = 1

while num != numero_aleatorio:
    intentos += 1
    num = int(input("Intenta de nuevo: "))

print("Adivinaste despues de ",intentos, "intento/s! El número era ", numero_aleatorio)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente

for i in range(100,-1,-2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero positivo: "))
suma = 0

for i in range(1, num+1):
    suma += i

print("La suma de los numeros enteros entre 0 y", num, "es: ", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant = 10
cant_pares = 0
cant_impares = 0
cant_negativos = 0
cant_positivos = 0

for i in range(0, cant):
    num = int(input("Ingrese un numero entero: "))
    if num < 0:
        cant_negativos += 1
    elif num > 0:
        cant_positivos += 1
    if num % 2 == 0:
        cant_pares += 1
    else:
        cant_impares += 1

print("Se ingresaron:")
print(cant_pares, "numeros pares.")
print(cant_impares, "numeros impares.")
print(cant_positivos, "numeros positivos.")
print(cant_negativos, "numeros negativos.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cant = 100
suma = 0

for i in range(0, cant):
    num = int(input("Ingrese un numero entero: "))
    suma += num

print("La media de los numeros ingresados es: ", suma / cant)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

from math import trunc

num = int(input("Ingrese un numero entero: "))
num_invertido = 0
cero_al_comienzo = ""

if num % 10 == 0:
    cero_al_comienzo = "0"

while num > 0:
    digito = num % 10
    num_invertido = num_invertido * 10 + digito
    num = trunc(num / 10)

print(f"El numero invertido es: {cero_al_comienzo}{num_invertido}")
