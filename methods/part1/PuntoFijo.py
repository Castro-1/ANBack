import numpy as np
import math

# Punto fijo

def punto_fijo(func_str, gfunc_str, x0, tol, max_iter, error):
    def current_error(x2, x1):
        if error == 0:
            return abs(x2 - x1)
        else:
            return abs(x2 - x1) / x2

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
        err = current_error(x1, x0)

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
