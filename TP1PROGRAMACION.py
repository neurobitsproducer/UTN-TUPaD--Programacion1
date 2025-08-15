#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”.



nombre=input("Ingrese su nombre: !")
print(f"hola {nombre} !")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”“Pérez”,“30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”.

nombre=input("Ingrese su nombre: !")
apellido=input("Ingrese su apellido: !")
edad=input("Ingrese su edad !")
residencia=input("Ingrese su lugar de residencia !")

print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro. 

radio =int(input("Ingrese el Radio de un circulo : "))
area = 3.14 * radio**2
perimetro = 2*3.14*radio

print(f"Su area es: {area} y su perimetro es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Indique cantidad de segundos"))
minutos = segundos / 60
horas = minutos / 60

print(f"equivale a: {horas} !")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un numero :"))

for i in range(1,10):
    print(f"{numero} * {i} = {numero * 1 } ")

# 7) CREAR UN Pograma que pida al usuario dos numeros enteros distintos a 0 y muestre 
#por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

num = int(input("Ingrese un numero mayor a cero: "))
num2 = int(input("Ingrese otro numero mayor a cero: "))

suma = num + num2
division = num / num2
multiplicacion = num * num2
resta = num - num2

print(f"El total de la suma es : {suma}")
print(f"El total de la division es : {division}")
print(f"El total de la multiplicacion es : {multiplicacion}")
print(f"El total de la resta es : {resta}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

peso = int(input("Ingrese su peso: "))
altura = int(input("Ingrese su altura: "))

imc = peso /(altura)**2

#print(f"Su indice de masa corporal es de: {imc} !")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. 

celsius = int(input("Ingrese temperatura en grado celcius: "))

fahrenheit = (9/5)*celsius+32
print(f"su equivalente en grados Fahrenheit es {fahrenheit} ")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num = int(input("ingrese un numero :"))
numdos = int(input("ingrese un segundo numero :"))
numtres = int(input("ingrese un tercer numero :"))

promedio = (num + numdos + numtres)/3

print(f"El promedios es de: {promedio} !")