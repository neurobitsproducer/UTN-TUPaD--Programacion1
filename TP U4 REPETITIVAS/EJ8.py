#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador = 10
pares = 0
impares = 0
negativos = 0
for i in range(contador):
    num = int(input("ingrese un numero"))
    if num < 0:
        negativos += 1
    elif num % 2 == 0:
        pares = pares +1
    else:
        impares += 1
print(f"Los numeros pares:({pares})")
print(f"Los numeros impares:({impares})")
print(f"Los numeros negativos:({negativos})")
