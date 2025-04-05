base = int(input("ingrese la base de la potencia"))
exponente = int(input("ingrese el exponente de la potencia"))
total = 0


# acumulador = 1
def pote ():
    for i in range(0,exponente):

        acumulador = acumulador*base


# print(acumulador)


n = 0
# acumulador = 1
def poteRecursiva ():
    # n = 0
    global n
    global acumulador
    n = n+1



    acumulador = acumulador*base
    if n == exponente:
        return acumulador
    else: poteRecursiva()


acumulador = 1
def poteRecursiva2 (base,exponente,acumulador):   #La sugerencia del profe fue que lo hicera pero recibiendo los parametros
# n = 0
    global n 
    n = n+1



    acumulador = acumulador*base
    if n == exponente:
        return acumulador
    else:
        # print("entre") 
        return poteRecursiva2(base,exponente,acumulador)



resultadoRecursividad = poteRecursiva2(base,exponente,acumulador)
print(f"El resultado de la funcion recursiva es{resultadoRecursividad}")