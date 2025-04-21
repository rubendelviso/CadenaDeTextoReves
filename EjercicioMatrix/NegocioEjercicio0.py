

import MenuEjercicio0 as menu
import UtilitiesEjercicio0 as utils
from UtilitiesEjercicio0 import matrix0,diagonal



decision = float('inf')

while decision != 7:
    if decision == 1:   
        utils.CargaManual()

    elif decision == 2:
        utils.MatrizRandom(matrix0)
    elif decision == 3:
        utils.mostrarMatriz()
    elif decision == 4:
        utils.ModificarMatriz()
    elif decision == 5:
        utils.PromedioDiagonal(diagonal)
    elif decision == 6:
        matrizMuestra = utils.menorDiagonal(matrix0)
        print(f"la matriz era:\n {matrix0}")
    decision = menu.menu()