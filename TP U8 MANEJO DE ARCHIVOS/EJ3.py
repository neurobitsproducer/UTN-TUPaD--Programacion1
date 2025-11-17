#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

import os

archivo_nombre = "productos.txt"

#muestro la lista
with open(archivo_nombre,"r")as archivo:
    for linea in archivo:
        datos= linea.strip().split()
        print(datos)

#pido los datos
with open(archivo_nombre,"a") as file:
    producto = input('Ingrese el nombre del producto: ')
    precio = input('Ingrese el precio del producto: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    file.write(f'{producto},{precio},{cantidad}\n')


    #muestro la lista
with open(archivo_nombre,"r")as archivo:
    for linea in archivo:
        datos= linea.strip().split()
        print(datos)