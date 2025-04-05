"""
Realiza un programa que permita ingresar las notas de un alumno para una cursada determinada.
Para ello el programa debe solicitar el nombre de la materia para la cual se cargaran las notas,
el DNI del alumno, el nombre y apellido del alumno y la cantidad de notas a cargar.
Debe solicitar que se ingrese nota por nota y luego debe mostrar por pantalla los datos del alumno,
la nota final de la materia teniendo en cuenta que esta es el promedio de todas las notas cargadas,
la nota más alta, y la nota más baja.
"""
# realize un programa que permite ingresar las notas de un alumno para una cursada detrminada.Para ello el programa
# debera solicitar nombre de la materia, dni del alumno, nombre y apellido del alumno y la cantidad de notas a cargar
# Debe solicitar que se ingrese nota por nota y luego debe mostrar por pantalla la nota final de la materia, teniendo
# en cuenta que es el promedio de todas las notas cargadas, la nota mas alta y la nota mas baja


materia= input("ingrese el nombre de la materia")
dni = int(input("ingrese el dni de la persona"))
notasCarga = int(input("ingrese la cantidad de notas a cargar"))
acuNota =0
# maximo = '+inf'
# maximo= 0
# minimo= '-inf'
# minimo = 0
promedio =0
nombreDeLaPersona = input("ingrese el nombree de la persona")

for i in range(0,notasCarga):
    nota = int(input("ingrese la nota"))
    acuNota+=nota
    if i ==0:
        maximo = nota
        minimo = nota

if nota>maximo:
    maximo = nota

if nota<minimo:
    minimo = nota


promedio=acuNota/notasCarga

print(f"el nombre de la materia es",materia, "el dni de la persona es",dni,"y el promedio es ",promedio )
print(f"la nota mas alta es ", maximo, "la nota mas baja es", minimo)
print(f"el nombre de la persona es",nombreDeLaPersona)