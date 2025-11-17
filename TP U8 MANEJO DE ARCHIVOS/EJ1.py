#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

import os

archivo_nombre = "productos.txt"
if not os.path.exists(archivo_nombre):
    with open(archivo_nombre,"w")as archivo:
        archivo.write("nombre,precio,cantidad\n")
        archivo.write("lapiz,25,100\n")
        archivo.write("goma,10,200\n")
        archivo.write("regla,15,50\n")

