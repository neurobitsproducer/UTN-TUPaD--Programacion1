#6)escribir un programa que tome la lista numeros
#aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros
#aleatorios de la siguiente forma:

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

import statistics

moda=statistics.mode(numeros_aleatorios)
promedio = statistics.mean(numeros_aleatorios) 
medio =statistics.median(numeros_aleatorios)


#Sesgo positivo o a la derecha: cuando la media(promedio) es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#Sesgo negativo o a la izquierda: cuando la media(promedio) es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#Sin sesgo: cuando la media, la mediana y la moda son iguales.

print(f"moda: {moda}\npromedio: {promedio}\nmedio: {medio}")

if promedio > medio and medio > moda:
    print("sesgo positivo o a la derecha")
elif promedio < medio and medio < moda:
    print("sesgo negativo o a la izquierda")
elif promedio == medio and medio == moda:
    print("sin sesgo")
else:
    print("no se puede determinar el sesgo")    