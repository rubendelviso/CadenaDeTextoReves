# Implementá una funcion recursiva que reciba una cadena de texto y devuelva su reverso.

# No está permitido usar slicing, ni funciones como reversed() o bucles.

# Por ejemplo:

# reverso_recursivo ("Hola") debería devolver "aloH"


PalabraReves = []
contador = 1
casoBase = input("ingrese la palabra que quiere poner de reves")
longitudCasoBase = len(casoBase)



def CadenaDeReves (casoBase,longitudCasoBase,contador):
    

#Estaba chequeando la logica en este punto unicamente

    
    # CasoBase =  input("ingrese la palabra que quiere dar vuelta")
    # longitudCasoBase = len(CasoBase)

    # PalabraReves = []
    # contador= 1
    # "print(len(CasoBase))"
    # while longitudCasoBase != contador:

    #     prueba0 = longitudCasoBase-contador

    #     char = CasoBase[prueba0]

    #     PalabraReves.append(char)
    #     contador+=1
        
    global PalabraReves
    # global contador
    


    
    #PalabraReves.append(longitudCasoBase-contador)
    

    Char = casoBase[longitudCasoBase-contador]
    PalabraReves.append(Char)

    # contador+=1

    if contador == longitudCasoBase:
        return PalabraReves
    else:
        return CadenaDeReves(casoBase,longitudCasoBase,contador+1)

    

    

print(CadenaDeReves(casoBase,longitudCasoBase,contador))