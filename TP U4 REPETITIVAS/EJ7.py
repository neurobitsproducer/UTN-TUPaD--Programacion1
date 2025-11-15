#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.


num = int(input("Ingrese un numero entero "))
for i in range(0,num):
    num += i

print(f"El total es : {num}")