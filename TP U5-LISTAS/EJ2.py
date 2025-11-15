#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista =[]
for i in range (1,6):#pido 5 productos
    productos = input("ingrese el producto a la lista".strip())
    lista.append(productos)

print()
lista = sorted(lista)#ordeno alfabeticamente
print(lista)#muestro lista
print()

while True:#bucle para quitar o no elemnetos de la lista
    quitar = input("Desea quitar un producto? Si/No")

    if quitar.lower() == "no":
        print("saliendo...")
        break

    while quitar.lower() == "si":
        print(lista)
        opcion = int(input("Elija el numero de elemento del 1 al 5").strip())
        #uso opcion numericas int.
        if 0<opcion<=len(lista):        
            lista.pop(opcion -1)#uso pop para remover por posicion indice

        #muestro la lista actual
        print(lista)
        print()

        quitar = input("Desea quitar otro producto? Si/No").lower().strip()

       