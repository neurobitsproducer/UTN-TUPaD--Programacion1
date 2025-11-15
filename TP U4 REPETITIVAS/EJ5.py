#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 
num = random.randint(0,9) 
contador = 0
while True:
    num_usuario = input("adivine un numero entre 0 y 9, ingrese un numero! ")
    if num_usuario.isdigit():
        num_usuario = int(num_usuario)
        contador += 1
        if num == num_usuario:
            print("felicitaciones adivinaste! 🥳")
            print(f"intentos Totales: {contador} 😅")
    else:
        print("ingrese solo numeros")