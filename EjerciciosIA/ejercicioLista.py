# Contar cuántas veces aparece un número en una lista

def listaDeNum ():
    listaDeNum = []
    Cantidad = int(input("Ingrese la cantidad de numeros que quiere ingresar"))
    for i in range(Cantidad):
        
        listaDeNum.append(int(input("ingrese el numero: ")))
        
    # LongitudLista = len(listaDeNum)
    return listaDeNum,Cantidad

# listaDeNum()
# contador= 1

NumRepetido = []
contadorDeRepetidos = 0
def contadorDeNum(listadeNum,longitud):

    msg = "Termino la recursion"
    global NumRepetido
    contadorDeRepetidos = 0 
    n = listadeNum[(longitud-1)]

    for i in range (longitud):
        if listadeNum[i]==n:
            contadorDeRepetidos+=1      

    if contadorDeRepetidos >= 2:   
        print(f"El numero {n} se repite {contadorDeRepetidos-1} veces")
    

    
    # print(listadeNum[longitud-1])           Solo una verificacion
    if longitud == 1:
        return msg
    else:
        return contadorDeNum(listadeNum,(longitud-1))

# def VerificarReps (listadeNum,longitud):
#     global NumRepetido, contadorDeRepetidos
#     n = listadeNum(longitud-1)
#     if n in listadeNum:
#        contadorDeRepetidos += 1 
    
#     if longitud == 1:
#         return Repeticiones
#     else:
        
#         return contadorDeNum(listadeNum,(longitud-1))

    



lista,longitud = listaDeNum()

repeticiones = contadorDeNum(lista,longitud)