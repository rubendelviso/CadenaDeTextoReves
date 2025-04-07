#Este ejercicio consta de verificar si una palabra es palindroma usando recursion
contador = 0
def cargarPalabra ():
    NuevaPalabra = []
    palabra = input("ingrese la palabra que quiere verificar")
    medidaPalabra = len(palabra)
    

    return NuevaPalabra,palabra,medidaPalabra


def palabraPalindroma (NuevaPalabra,palabra,medidaPalabra):
    global contador,verificacion
    if medidaPalabra == 1 and verificacion == True:
        print("la palabra es palindroma felicidades")
        dec = input("si desea ingresar otra palabra presione 1, de lo contrario presione cualquier otra tecla")
        if dec == 1:
            CargaFunciones()
        else:
            print("fin")
            return NuevaPalabra
        
             
    
    verificacion = False
    charOrig = palabra[contador]
    charReves = palabra[medidaPalabra-1]
    # NuevaPalabra.append(charReves)
    contador+=1
    if charOrig != charReves:
        print("La palabra no es palindroma, Ingrese otra palabra por favor")
        return CargaFunciones()
    
    else:
        verificacion = True
        return palabraPalindroma (NuevaPalabra,palabra,medidaPalabra-1)
        
        

    
def CargaFunciones ():    

    NuevaPalabra,palabra,medidaPalabra = cargarPalabra()

        

    NuevaPalabra = palabraPalindroma(NuevaPalabra,palabra,medidaPalabra)

CargaFunciones()