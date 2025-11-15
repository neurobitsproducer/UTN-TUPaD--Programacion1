#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana

#listas de las minimas
tem_minimas = [10,8,12,15,19,20,17,]

#lista de las maximas 
tem_maximas = [25,27,28,29,30,33,34]

#matriz de las sublistas
matriz = [tem_minimas,tem_maximas]

#imprimo por pantalla
#cantidad de filas
cantidad_filas = len(matriz)#cantidad de filas = a la cantidad de sublistas
#cantidad columnas es igual a la cantidad de elemntos dentro de una lista
cantidad_columnas = len(matriz[0])

for i in range(cantidad_filas):
    print(matriz[i])