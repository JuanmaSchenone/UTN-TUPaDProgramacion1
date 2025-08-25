# Actividades
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

print("Saludo 1")
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

print("Saludo 2")
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

print("Area y perimetro de un circulo")
radio = input("Por favor, ingrese el radio del círculo: ")
area = 3.14 * (int(radio) ** 2)
perimetro = 2 * 3.14 * float(radio)
print(f"El área del círculo es: {area}, y su perímetro es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

print("Convertir segundos a horas")
segundos = input("Por favor, ingrese una cantidad de segundos: ")
horas = int(segundos) / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = input("Por favor, ingrese un numero:")
print(f"Tabla de multiplicar de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {int(numero) * i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Ingrese a continuacion 2 numeros distintos de cero")
num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Resultados de operaciones para los numeros {num1} y {num2}:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) ** 2

print("Calculo de IMC")
peso = float(input("Por favor, ingrese su peso en kg: "))
altura = float(input("Por favor, ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5 * celsius) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

print("Calculo del promedio de 3 numeros.")
num1 = float(input("Por favor, ingrese el primer número: "))
num2 = float(input("Por favor, ingrese el segundo número: "))
num3 = float(input("Por favor, ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números ingresados es: {promedio}")
