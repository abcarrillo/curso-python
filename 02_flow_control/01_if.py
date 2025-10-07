###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.
edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del if
print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 5

# Además de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si está presente)
if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript: 
# && sería and
# || sería or

# En el caso que seas mayor de edad y tengas carnet...
# entonces podrás conducir
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")

# En un pueblo de Isla Margarita son más laxos y
# te dejan conducir si eres mayor de edad O tienes carnet
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

# También tenemos el operador lógico "not"
# que nos permite negar una condición
es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

# Más fácil sería:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
  print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
  print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
  print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

#print("------------------------", "\n")
#print(" Ejercicio 1 ", "\n")

#numero_1 = input("Introduce número 1: ")
#numero_2 = input("Introduce número 2: ")

#if numero_1 > numero_2:
#  print(f"El numero {numero_1} es mayor que {numero_2}")
#elif numero_2 > numero_1:
#  print(f"El numero {numero_2} es mayor que {numero_1}")
#else:
#  print("Los numeros son iguales")



# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
'''
print("------------------------", "\n")
print(" Ejercicio 2 ", "\n")

operador_1 = float(input("Introduce operador 1: "))
operador_2 = float(input("Introduce operador 2: "))
signo = input("Introduce el signo de la operación (+, -, *, /): ")

if signo == "+":
  print(f"SUMA - Resultado: {operador_1 + operador_2}")
elif signo == "-":
  print(f"RESTA - Resultado: {operador_1 - operador_2}")
elif signo == "*":
  print(f"MULT - Resultado: {operador_1 * operador_2}")
elif signo == "/":
  print(f"DIV - Resultado: {operador_1 / operador_2}")
else:
  print("No reconozco ese signo")
'''

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

'''
print("------------------------", "\n")
print(" Ejercicio 3 ", "\n")

year_input = input("Introduzca un año para comprobar si es bisiesto: ")

if (year_input % 4 == 0 and year_input % 100 != 0) or year_input % 400 == 0:
    print(f"{year_input} es un año bisiesto.")
else:
    print(f"{year_input} no es un año bisiesto.")
'''



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("------------------------", "\n")
print(" Ejercicio 4 ", "\n")

age_input = int(input("Introduzca su edad:"))

if(age_input >= 0 and age_input <= 2):
  print("Bebé (0-2 años)")
elif(age_input >= 3 and age_input <= 12):
  print("Niño (3-12 años)")
elif(age_input >= 13 and age_input <= 17):
  print("Adolescente (13-17 años)")
elif(age_input >= 18 and age_input <= 64):
  print("Adulto (18-64 años)")
elif(age_input >= 65):
  print("Adulto mayor (65 años o más)")
else:
  print("Edad no válida")