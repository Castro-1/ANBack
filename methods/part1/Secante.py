import numpy as np
import math
import matplotlib.pyplot as plt

def secante(func_str, x0, x1, tol, niter, error):
    def current_error(x2,x1):
        if error == 0:
            return abs(x2-x1)
        else:
            return abs(x2-x1)/x2


    # Convierte el string en una función ejecutable
    func = lambda x: eval(func_str)

    resultados = {
        "found": None,
        "x": [],
        "f": [],
        "e": []
    }

    for i in range(niter):
        f_x1 = func(x1)
        f_x0 = func(x0)

        # Cálculo de la siguiente aproximación
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        # Cálculo del error relativo
        err = current_error(x2,x1)

        # Almacenar resultados en el diccionario
        resultados["x"].append(x2)
        resultados["f"].append(func(x2))
        resultados["e"].append(err)

        # Comprobar convergencia
        if err < tol:
            resultados["found"] = 1
            break
        elif i == niter - 1:
            resultados["found"] = 0

        # Actualizar valores para la siguiente iteración
        x0 = x1
        x1 = x2

    return resultados


# secante("x**3 - 2*x**2 - 5", 1.0, 2.0, 1e-6, 100, 0)