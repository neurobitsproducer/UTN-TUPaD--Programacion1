#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

import random
cantidad = 7

lista = []
lista_invertida = []

#genero 7 numeros al azar
for i in range(cantidad):
    numero = random.randint(1,100)
    lista.append(numero)

#imprimo la lista 
print(lista)

#reacomodo en nueva lista desde el ultimo indice
for i in range(cantidad):
    lista_invertida.append(lista[-1+i])
    
#muestro lista re ordenada
print(lista_invertida)