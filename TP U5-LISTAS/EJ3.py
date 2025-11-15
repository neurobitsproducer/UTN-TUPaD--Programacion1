#Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

import random

cantidad = 15
lista_par = []
lista_impar = []

for i in range(cantidad):
    numeros = random.randint(1,100)
    if numeros%2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)

print(lista_par)
print(lista_impar)
print()

par = len(lista_par)
impar = len(lista_impar)

print(f"cantidad par: {par}")
print(f"cantidad impar: {impar}")