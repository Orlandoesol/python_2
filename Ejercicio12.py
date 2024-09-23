# Lea N calificaciones de un grupo de alumnos, calcule y escriba el porcentaje de
# reprobados, tomando en cuenta que la calificación mínima aprobatoria es de 70.

reprobados = 0
i = 0
n = int(input('Cantidad de alumnos: '))
while(i < n):
    nota = float(input(f'Ingrese la nota del alumno {(i+1)}: '))
    if(nota < 70):
        reprobados +=1
    i+=1
print('El porcentaje de reprobados es: ', (reprobados / n) * 100, "%")
