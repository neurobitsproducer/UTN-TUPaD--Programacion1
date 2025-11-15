#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

while True:
    num_uno = input("ingrese un numero entero: ")
    num_dos = input("ingrese otro numero entero: ")
    if num_uno.isdigit() == True and num_dos.isdigit() == True:
        num_uno = int(num_uno)+1
        num_dos = int(num_dos)
        break
    else:
        print("ingreso no valido, ingrese solo numeros !")

suma = 0
for i in range(num_uno,num_dos):
    print(i)
    suma += i
print(f"La suma total es de :{suma} ")