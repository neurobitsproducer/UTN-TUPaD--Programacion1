#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:

#Menor que 3: "Muy leve" (imperceptible).
#Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

clase_magnitud = int(input("clasifique la magnitud de un terremoto segun la escala de Richter: \n menor que 3:\n Mayor o igual que 3 y menor que 4 \n Mayor o igual que 4 y menor que 5:\n Mayor o igual que 5 y menor que 6:\n Mayor o igual que 6 y menor que 7:\n Mayor o igual que 7: " ))

if clase_magnitud < 3:
    print("Muy leve (imperceptible)")
elif clase_magnitud >= 3 and clase_magnitud <= 4:
    print("Leve (ligeramente perceptible).")    
elif clase_magnitud >= 4 and clase_magnitud <= 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif clase_magnitud >=5 and clase_magnitud <= 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif clase_magnitud >= 6 and clase_magnitud <= 7:
    print("Muy Fuerte  (puede causar daños significativos).")
elif clase_magnitud > 7:
    print("Extremo (puede causar graves daños a gran escala).")
else :
    print("numero invalido") 