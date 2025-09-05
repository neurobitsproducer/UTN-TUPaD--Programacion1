# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("en cuál hemisferio se encuentra 'NORTE' o 'SUR' (N/S)").lower()
mes = int(input("Seleccione el numero del mes que esta: \n(1):ENERO \n(2):FEBRERO \n(3):MARZO \n(4):ABRIL \n(5):MAYO \n(6):JUNIO \n(7):JULIO \n(8):AGOSTO \n(9):SEPTIEMBRE \n(10):OCTUBRE \n(11):NOVIEMBRE \n(12):DICIEMBRE "))
dia = int(input("Indique el numero del dia: "))

print(hemisferio , mes , dia )

if hemisferio =="n" or hemisferio =="norte":
    if  dia >= 21 and mes == 12:
        print("Invierno!")
    elif mes == 1 or mes ==2 or (mes == 3 and dia <= 20):
        print("Invierno!")
    elif dia >= 21 and mes == 3:
        print("Primavera!")
    elif mes == 4 or mes ==5 or (mes == 6 and dia <= 20):
        print("Primavera!")    
    elif dia >= 21 and mes == 6:
        print("Verano!")
    elif mes == 7 or mes ==8 or (mes == 9 and dia <= 20):
        print("Verano!")
    elif dia >= 21 and mes == 9:
        print("Otoño!")
    elif mes == 10 or mes ==11 or (mes == 12 and dia <= 20):
        print("Otoño")


if hemisferio =="s" or hemisferio =="sur":
    if  dia >= 21 and mes == 12:
            print("Verano!")
    elif mes == 1 or mes ==2 or (mes == 3 and dia <= 20):
            print("Verano!")
    elif dia >= 21 and mes == 3:
            print("Otoño!")
    elif mes == 4 or mes ==5 or (mes == 6 and dia <= 20):
            print("Otoño!")    
    elif dia >= 21 and mes == 6:
            print("Invierno!")
    elif mes == 7 or mes ==8 or (mes == 9 and dia <= 20):
            print("Invierno!")
    elif dia >= 21 and mes == 9:
            print("Primavera!")
    elif mes == 10 or mes ==11 or (mes == 12 and dia <= 20):
            print("Primavera!")
