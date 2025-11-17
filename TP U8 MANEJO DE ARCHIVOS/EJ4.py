#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

archivo_nombre = "productos.txt"

# lista donde guardaré los diccionarios
productos = []  

with open(archivo_nombre, "r") as archivo:
    for line in archivo:
        producto, precio, cantidad = line.strip().split(',')
        productos.append({
            'nombre': producto,
            'precio': precio,
            'cantidad': cantidad
        })

print(productos)

