import MenuEjercicio0 as menu
import numpy as np
import random as rndm



matrix0 = np.zeros([5,5],dtype=int)
#Aca empiezan las utilidades
diagonal  = np.diag(matrix0)
def CargaManual ():
#inicializo la variable
    # matrix0 = np.zeros([3,3],dtype=int)
    
    global matrix0
    
    for fila in range(0,len(matrix0)):
        
        for col in range(0,len(matrix0[0])):


            matrix0[fila,col] = input(f"ingrese el numero en la fila{fila}\nColumna: {col}\nNro = ")     

    return matrix0


"Cargar la matriz de forma automática (Esta función debe cargar todas las posiciones de la matriz con números aleatorios)."

def MatrizRandom (matrix0):

    
    for fila in range(0,len(matrix0)):
        
        for col in range(0,len(matrix0[0])):

            matrix0[fila,col] =rndm.randint(1,100)


    print(matrix0)
    return matrix0


"Mostrar matriz (Debe imprimir en formato de tabla los datos cargados en la matriz)."
def mostrarMatriz ():
    print(matrix0)

# Modificar matriz (Debe solicitar al usuario la posición a modificar y,
# en caso de estar dentro de los límites de la matriz, pedir el nuevo valor numérico a guardar en dicha posición).
def ModificarMatriz ():
    OutofIndex = ""

    while OutofIndex != False:
        
        posicionCol = int(input("ingrese el indice de la columna que quiere modificar"))
        
        posicionFila = int(input("ingrese el indice de la fila que quiere modificar"))
        if posicionCol>len(matrix0) or posicionFila>len(matrix0[0]):
            print("Te pasaste pa, escribilo de nuevo")
        else:
            OutofIndex = False  
    Objeto = int(input("ingrese el valor del objeto que quiere indexar en esa posicion"))
#Recordar que el valor del indice de la fila va 1° ------> 2° en seguida va la posicion de la columna
    
    matrix0[posicionFila,posicionCol] = Objeto

    mostrarMatriz()

    
def PromedioDiagonal (diagonal):
    TotalDiagonal = 0
    #diagonal  = np.diag(matrix0)
    for i in range (0,len(diagonal)):
        TotalDiagonal += diagonal[i]

    TotalDiagonal/= len(diagonal)

    print(f"El promedio de la diagonal es: {TotalDiagonal}")

 #último indice de una lista es su longitud menos 1

def menorDiagonal (matrix0):  #es el de la contradiagonal lpm
 "Pense q era de la diagonal pero  no"
    # minimo = float('inf')
    # for i in range(0,len(diagonal)):
    #     #valorpRUEBA = diagonal[i]
    #     #print ("valor,",valorpRUEBA)
    #     if diagonal[i]<minimo:
    #         minimo = diagonal[i]
    
    # print(f"El numero mas pequeño de la diagonal es:{minimo}")

 #es de la contradiagonal
#  print(matrix0)

#  print("matrix0[0]:", matrix0[0])

#  print("type(matrix0[0]):", type(matrix0[0]))


 

 ultimoValorFila = (len(matrix0)-1)
 ultimoValorColumna = (len(matrix0[0])-1)
 contradiagonal = []
 
 acuCol = 0
 acuFil = 0
 for i in range (0,len(matrix0)):  #fila
        
        for j in range (0,len(matrix0[0])): #columna
            
            # print(matrix0[i][ultimoValor])


            # ultimoValor-=1

        
            if i==0 and j == ultimoValorColumna:


                ultimoValorFila=i
                ultimoValorColumna=j
                contradiagonal.append( matrix0[i][ultimoValorColumna])
                
                ultimoValorColumna-=1
                ultimoValorFila+=1
                 
                
            elif i == ultimoValorFila and j == ultimoValorColumna:
                ultimoValorFila=i
                ultimoValorColumna=j

                contradiagonal.append( matrix0[i][ultimoValorColumna])

                ultimoValorColumna-=1
                ultimoValorFila+=1

                

            elif i == ultimoValorFila and j == ultimoValorColumna:
                
                ultimoValorFila=i
                ultimoValorColumna=j

                contradiagonal.append( matrix0[i][ultimoValorColumna])

                ultimoValorColumna-=1
                ultimoValorFila+=1                
                
                

            elif i == ultimoValorFila and j == ultimoValorColumna:
                
                ultimoValorFila=i
                ultimoValorColumna=j

                contradiagonal.append( matrix0[i][j])

                ultimoValorColumna-=1
                ultimoValorFila+=1                
                
                            
            elif i == ultimoValorFila and j == ultimoValorColumna:
                
                ultimoValorFila=i
                ultimoValorColumna=j
                contradiagonal.append( matrix0[i][j])
                ultimoValorColumna-=1
                ultimoValorFila+=1                
 conversorInt(contradiagonal)             
                
            

                    
#  list(contradiagonal)
#  conversorInt(contradiagonal)


    
#  promedio = acu/len(contradiagonal)s
#  print(f"el promedio es {promedio}")
     
def conversorInt (contradiagonal):
    acuEnteros = 0
    contradiagonalEnteros = []
    
    for i in range (0,len(contradiagonal)):
        numero = int(contradiagonal[i])

        contradiagonalEnteros.append(numero)
        # acuEnteros+= contradiagonalEnteros[i]

    # promedio = acuEnteros/len(contradiagonal)
    # print(f"el promedio es {promedio}")

    print(f"el numero minimo es{min(contradiagonalEnteros)}")
    return matrix0

# mat = MatrizRandom(matrix0)
# menorDiagonal(mat)
    
    

# "Modificar matriz (Debe solicitar al usuario la posición a modificar y, en caso de estar dentro de los límites de la matriz"
# "pedir el nuevo valor numérico a guardar en dicha posición)."
# menorDiagonal(matrix0)



def FilaCeros (matrix0):
    

    FilaMod= int(input("Ingrese la fila que quiere modificar"))
    #Sobrescribir fila con ceros (esto debe solicitar al usuario cual fila quiere modificar y 
    #debe reemplazar todos los valores de esa fila con 0)
    for i in range (0,len(matrix0)):
        for j in range(0,len(matrix0[0])):
            if i == FilaMod:
                ValorCero = 0
                matrix0[i][j] = ValorCero

    print(matrix0)

#Sobrescribir columna con -1 (esto debe solicitar al usuario cual columna quiere modificar
#y debe reemplazar todos los valores de esa columna con -1)

def ColumnaMenos (matrix0):
    FilaCol= int(input("Ingrese la columna que quiere modificar"))
    #Sobrescribir fila con ceros (esto debe solicitar al usuario cual fila quiere modificar y 
    #debe reemplazar todos los valores de esa fila con 0)
    for i in range (0,len(matrix0)):
        for j in range(0,len(matrix0[0])):
            if j == FilaCol:
                ValorCero = -1
                matrix0[i][j] = ValorCero

    print(matrix0)



rndma = MatrizRandom(matrix0)
ColumnaMenos(rndma)
