#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
#dio como parámetro y devuelva el área del círculo. calcular_peri-
#metro_circulo(radio) que reciba el radio como parámetro y devuel-
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
#bas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3,14 * (radio^2)
    print(area)
    return area


def calcular_perimetro_circulo(radio):
    perimetro = 2*3,14*radio
    print(perimetro)
    return perimetro

radio = int(input(" ingrese el radio del circulo"))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)