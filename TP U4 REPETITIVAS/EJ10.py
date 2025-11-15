#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num =(input("ingrese un numero entero! "))#trabajo por string
ultimo =""
invertido = ""
while   num != "":
    ultimo = num[-1] #tomo el ultimo caracter en la posicion -1
    invertido = invertido + ultimo # lo acumulo 
    num =num[:-1] #recorto el ultimo caracter para achicar el string
    
print(invertido)  
    