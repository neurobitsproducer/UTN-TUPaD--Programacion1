#8)Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia.

notas =[[8,5,9],#estudiante 1
        [7,7,8],#estudiante 2
        [6,6,7],#estudiante 3
        [4,8,9],#estudiante 4
        [6,5,8]]#estudiante 5

print(notas)   

#promedios estudiantes
#i para recorrer cada estudiante 
for i, estudiante in enumerate(notas, 1):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {estudiante} → Promedio: {promedio:.2f}")

