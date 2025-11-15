#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notas =[4,6,6,8,7,9,4,6,7,7]
print(notas)

total = 0
#total =sum(notas)
for i in notas: #i toma el valor de cada elemento de mi lista
    total += i #suma de valores
    

import statistics #uso libreria que vimos en otra unidad 
promedio = statistics.mean(notas)
print (f"La suma total es: {total}")
print (f"El promedio es : {promedio}")
