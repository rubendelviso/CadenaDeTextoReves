MenuTXT = """ Cargar matriz manualmente (Esta función debe solicitar al usuario el número a guardar en cada posición de la matriz).
 Cargar la matriz de forma automática (Esta función debe cargar todas las posiciones de la matriz con números aleatorios).
 Mostrar matriz (Debe imprimir en formato de tabla los datos cargados en la matriz).
 Modificar matriz (Debe solicitar al usuario la posición a modificar y, en caso de estar dentro de los límites de la matriz, pedir el nuevo valor numérico a guardar en dicha posición).
 Mostrar el promedio de la diagonal principal.
 Mostrar el menor de los números de la contradiagonal
 Salir del programa"""


def menu ():
    


    dec = int(input("A continuacion se mostrara el menu \n1)Cargar Matriz manualmente\n2)Cargar la matriz automaticamente\n3)Mostrar Matriz\n4)Modificar matriz\n5)Mostrar promedio de la diagonal principal\n6)Mostrar el menor de la contradiagonal\n7)Salir del programa"))

    
        
    return dec 
    

#Sobrescribir fila con ceros (esto debe solicitar al usuario cual fila quiere modificar y 
# debe reemplazar todos los valores de esa fila con 0)
#Sobrescribir columna con -1 (esto debe solicitar al usuario cual columna quiere modificar
#y debe reemplazar todos los valores de esa columna con -1)
