#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
total = 0
while True:
    print()
    num = input(" ingrese numeros enteros, para sumar !!!🤯 ")
    print(" Escriba 0 para salir !!! 🙈 ")

    if num.isdigit():# valido. numeros
        num = int(num)
        total += num # sumo los inputs
        
        if num == 0: #para salir y sumar
            
           print(f"la suma total es de:{total}  !!!🤯")
           break
 
    else:  
        print("ingrese solo numeros enteros !!! ")

    
        
