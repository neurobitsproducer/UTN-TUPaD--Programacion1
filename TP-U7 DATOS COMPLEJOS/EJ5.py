#Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
#Ejemplo:
#Entrada -> "hola mundo hola"
#Salida ->
#    palabras_unicas: {'hola', 'mundo'}
#    recuento: {'hola': 2, 'mundo': 1}

#pido frase
frase = input('Ingrese una frase: ')

#valido palabras unicas 
palabras_unicas = set(frase.split())

recuento = {}

palabras = frase.split()
for palabra in palabras:
    recuento[palabra] = palabras.count(palabra)

#imprimo 
print(palabras_unicas)
print(recuento)