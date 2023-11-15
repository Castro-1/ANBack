import numpy as np
import math
from methods.part1.features import current_error
# Punto fijo

def punto_fijo(func_str, gfunc_str, x0, tol, max_iter, error):

    resultados = {
        "found": None,
        "x": [],
        "f": [],
        "e": []
    }

    gfunc = lambda x: eval(gfunc_str)
    func = lambda x: eval(func_str)

    for i in range(max_iter):
        f = func(x0)
        x1 = gfunc(x0)
        err = current_error(x1, x0,error)

        # Almacenar resultados en el diccionario
        resultados["x"].append(x1)
        resultados["f"].append(f)
        resultados["e"].append(err)

        if err < tol:
            resultados["found"] = 1
            break
        elif i == max_iter - 1:
            resultados["found"] = 0

        x0 = x1

    return resultados

# print(punto_fijo("(10 / (x + 2)**(1/2))", 4.0, 1e-6, 100, 0))
