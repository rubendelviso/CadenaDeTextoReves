#Generar todas las permutaciones de una cadena 

#Recordar que todas las permutaciones vienen dadas siempre por la cantidad de objetos dados

import random
palabraOriginal = ""

def cargaDeCadena():
    global palabraOriginal
    palabraOriginal = input("ingrese la palabra que quiere")

    factorial = len(palabraOriginal)
    CasoBase = permutacionesPosibles(factorial)
    

contador = 0
resultadoFactorial = 1
def permutacionesPosibles (factorial):
    global resultadoFactorial

    

    resultadoFactorial*=factorial

    if factorial !=1: 
        return permutacionesPosibles(factorial-1)
    else:


        return ObtenerPermutacion(resultadoFactorial)
    

ListaOriginal = []    

def ObtenerPermutacion (resultadoFactorial):
    CasoBase = resultadoFactorial   #no se tendria que pisar este

    global ListaOriginal

    permutacion = chequearComparacion(palabraOriginal,ListaOriginal)
    
    ListaOriginal.append(permutacion)

    resultadoFactorial-=1
    if CasoBase != 1:
        return ObtenerPermutacion (resultadoFactorial)
    else:
        print(f"la lista de posibilidades es {ListaOriginal}")

def chequearComparacion (posibilidad,listaOriginal):
    
    
    posibilidad = list(posibilidad)
    
    random.shuffle(posibilidad)

    posibilidad =''.join(posibilidad)

    if posibilidad in listaOriginal:
        return chequearComparacion(posibilidad,listaOriginal)
    else:
        return posibilidad

    
    

cargaDeCadena()
