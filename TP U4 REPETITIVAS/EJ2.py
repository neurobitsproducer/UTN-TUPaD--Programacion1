#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

while True:
    num_usuario = (input(" introduzca un numero entero: ")).strip() #elimino espacios del inicio o final
    if num_usuario.isdigit() == True: #valido que sea un numero entero
        digitos = len(num_usuario)# pido la longitud del string
        num_usuario = int(num_usuario)# guardo valor como entero
        
        break
    else:
  
        print("ingrese solo numeros")

print()
print(f"El numero ingresasdo tiene digito/s: {digitos} ")



