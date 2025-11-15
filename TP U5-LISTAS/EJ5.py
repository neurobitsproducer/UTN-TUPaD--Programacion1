#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

nombres = ["Ana", "Juan", "María", "Carlos", "Laura", "Pedro", "Sofía", "Diego"]

while True:
    #muestro la lista 
    print(". LISTA ESTUDIANTES. :  ")
    print(nombres)
    print("*"*50)

    #pregunto al usuario si quiere agregar/quitar
    option = input(" Indique las opciones del Menu :\n (1)para agregar un nombre : \n (2) quitar un nombre de la lista \n (3) para salir del menu ").strip().lower()
    print("*"*50)

    #valido la opcion 
    if option.isdigit():
        option = int(option)
    else:
        print(" la opcion no es valida !")


    match option:
        
        case 1:
            agregar_nombre = input(" escriba el nombre: ").strip().title()
            nombres.append(agregar_nombre)#agrego el nombre
            print(" agregado correctamente " )
            print(nombres)


        case 2:
            quitar_nombre = input(" que nombre desea quitar ? ").strip().title()
            #recorro la lista para quitar 
            if quitar_nombre in nombres:    
                nombres.remove(quitar_nombre)
                print(" nombre eliminado correctamente !")
            else:
                print(" No se encontro nombre en la lista!")
                   
        case 3:
            print("saliendo del programa 👀")
            break
        
        case _:
            print("opcion invalida, debe seleccionar 1,2 o 3")
