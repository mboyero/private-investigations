"""
def loop(a,b):
    while b > 0:
        print(a, end='\n')
        b = b - 1

name = input("Nombre: ") # Phyton por defecto convierte input a string
veces = input("Número de veces: ")
veces = int (veces) # Convertimos a int
print(loop(name, veces))

name2 = input("Nombre: ") # Phyton por defecto convierte input a string
print(name2, " tiene ", len(name2), " caracteres")

----
def operationMath ():
  print((3+2/2*5)**2)

operationMath()

----
def salary (a,b):
  print("The salary to be paid is", a*b, "€")

hours = input ("Hours: ")
hours = int (hours)
euro = input ("Euro per hour: " )
euro = int (euro)

salary (hours, euro)

----
def mayorEdad (a):
  if a >= 18:
    print("Es mayor de edad")
  else: print("No es mayor de edad") 

edad = int(input("Edad: "))

mayorEdad (edad)
----
def comprobar(intent, passw):
  if intent == passw:
    print("Contraseña correcta!")
  else:
    print("Contraseña incorrecta!")

password = 'hola'
intento = input(print("Introduzca contraseña: "))
comprobar (intento, password)
----
def division (a,b):
  c = float(a/b)
  print("El resultado es: ", c)

dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))

if divisor == 0:
  print("Error")
else:
  division(dividendo,divisor)
----

num = int(input("Número: "))

def parImpar (a):
  if a % 2 == 0:
    print("El número " + str(a) + " es par")
  else:
    print("El número " + str(a) + " es impar")

parImpar(num)
----

edad = int(input("Introduzca edad: "))
ingresos = float(input("Introduzca ingresos: "))

def tributar(edad, ingresos):
  if edad >= 18 and ingresos >= 1000:
    print("Tiene que tributar")
  else:
    print("No tiene que tributar")

tributar(edad,ingresos)
----

pizzaVeg = (input("¿Quiere una pizza vegetariana? (Sí/No): "))

def ingredientes (pizza):
  if pizzaVeg == "Sí":
    ingredienteVeg = input("Elija el ingrediente que quiera: Pimiento o Tofu: ")
    print("Pizza vegetariana: tomate, mozarella,", ingredienteVeg)
  else:
    ingredienteNormal = input("Elija el ingrediente que quiera: Peperoni, Jamón o Salmón: ")
    print("Pizza de persona normal: tomate, mozarella,", ingredienteNormal)

ingredientes(pizzaVeg)
----

palabra = input("Introduzca una palabra: ")
a = 0
while a < 10:
  print(palabra)
  a = a+1
----

cantidad = float(input("Cantidad a invertir: "))
años = int(input("Años de inversión: "))
interes = float(input("% Tasa de interés anual: "))

i = 0
while i < años:
  cantidad = cantidad*(1+interes/100)
  i=i+1
  print("Dinero acumulado en el año ", str(i),": ", str(cantidad))

alturaTri = int(input("Altura del triángulo: "))

for i in range(alturaTri):
  for j in range(i+1):
    print("*", end="")
  print("")

for i in range(alturaTri):
  print("*"*(i+1))

----

alturaTri = int(input("Número base del triángulo: "))

for i in range(1, alturaTri+1, 2):
  for j in range(i, 0, -2):
    print(j, end=" ")
  print("")

----
"""
num = int(input("Número: "))
i = 2 # Divisores

while num % i != 0:
  i += 1
if i == num:
  print("El número " + str(num) + " es primo")
else:
  print("El número " + str(num) + " no es primo")

