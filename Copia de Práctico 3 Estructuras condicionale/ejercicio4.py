#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:

#Niño/a: menor de 12 años.
#Adolescente: mayor o igual que 12 años y menor que 18 años.
#Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#Adulto/a: mayor o igual que 30 años.

edad2 = int(input("ingrese su edad: "))

if edad2 >= 0 and edad2 < 130:

    if edad2 < 12:
        print("es un Niño/a ")
    elif edad2 >= 12 and edad2 < 18:
        print("es Adolescente ")
    elif edad2 >=18 and edad2 < 30:
        print("es adulto/a joven ")
    else: 
        print("es adulto/a mayor ")
else: 
    print("edad invalida")