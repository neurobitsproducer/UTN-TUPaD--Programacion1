#Dada una lista con valores repetidos:
datos =[1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

#muestro lista original
print(" lista original: ")
print(datos)
print()

#paso mi lista a un conjunto que por defecto no retipe datos
datos = set(datos)#conjuntos

datos_sinduplicados = list(datos)#paso nuevamenta a una lista
#muestro el resultado final
print(" Lista sin duplicados: ")
print(datos_sinduplicados)