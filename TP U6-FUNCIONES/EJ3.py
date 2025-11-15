#3 Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
#dir los datos al usuario y llamar a esta función con los valores in-
#gresados.

def informacion_personal(nombre, apellido,edad,residencia):
    mostrar_info = print(f"Soy{nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    return mostrar_info

nombre = input("ingrese su nombre ").strip()
apellido = input("ingrese su apellido ").strip()
edad = input("ingrese su edad ").strip()
residencia = input("ingres pais de residencia !").strip()

informacion_personal(nombre,apellido,edad,residencia)