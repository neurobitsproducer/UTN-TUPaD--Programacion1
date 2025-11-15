#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

contador = 10
suma = 0
promedio = 0
for i in range(contador):
    num = int(input("ingrese un numero entero "))
    suma += num
    print (f'la suma :{suma}')
    promedio = suma / (i+1)
    print (f'el promedio : {promedio}')