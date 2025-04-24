#Este script se va a tratar de calcular el decimal a un numero binario con RECURSION


# CantidadDeElementos = int(input("Ingrese la cantidad de elementos que quiere ingresar en esta lista"))

def cargaDeDecimal ():
    listaBinaria = []

    Decimal = int(input("Ingrese el numero decimal que quiere calcular"))

    
    binario=ResDivisionYResto(listaBinaria, Decimal)

    # ListaResto.append(Resto)


    # if cantidadDeElementos == 0:   #casoBase
    #     return 
    # else:
    #     return cargaDeDecimal(cantidadDeElementos-1) 




    
def ResDivisionYResto(listaBinaria,decimal):
    CasoBase = 1

    Division= decimal / 2   #Cociente (resultado de la division)

    Resto = decimal % 2 

    listaBinaria.append(Resto)
    #convertir resto en entero
    if Resto:

        ListaDeEliminar = []
        # Resto = int(Resto) no funciono
        Resto= str(Resto)
        ListaDeEliminar.append()    

        medidaLista

        if ListaDeEliminar[1]
        
        

        
    if Division == CasoBase or Division<CasoBase:
        return listaBinaria()
    else: 
        return ResDivisionYResto(listaBinaria, Division)

    
def ListaReves(lista):

    largoLista = len (lista)
    
    lista.append(largoLista-1)


    if largoLista < 1:
        return lista
    else:
        return ListaReves(largoLista-1)
    


cargaDeDecimal()