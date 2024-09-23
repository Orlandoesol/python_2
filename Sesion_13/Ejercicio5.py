estudiantes = {}
cantidad = int(input('Cantidad de estudiantes: '))
for i in range(cantidad):
    estudiante = input('Nombre: ')
    while estudiante in estudiantes:
        print('El estudiante se encuentra registrado')
        estudiante = input('Nombre: ')
    notas = []
    nota = float(input('Nota del estudiante: '))
    while nota > 0:
        notas.append(nota)
        nota = float(input('Nota del estudiante(Si coloca una nota negativa, termina): '))
    estudiantes[estudiante] = notas.copy()
    
    for estudiante, notas in estudiantes.items():
        print('El promedio es: ',(estudiante, sum(notas)/len(notas)))