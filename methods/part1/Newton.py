
import numpy as np
import math
import matplotlib.pyplot as plt

def newton(func_str, x0, tol, niter, error):
    def current_error(x1, x0):
        if error == 0:
            return abs(x1 - x0)
        else:
            return abs(x1 - x0) / x1

    # Convierte el string en una función ejecutable
    func = lambda x: eval(func_str)

    resultados = {
        "found": None,
        "x": [],
        "f": [],
        "e": []
    }

    for i in range(niter):
        f_x0 = func(x0)
        f_x0_prime = (func(x0 + tol) - f_x0) / tol  # Cálculo del gradiente

        if f_x0_prime == 0:
            resultados["found"] = -1
            break

        # Cálculo de la siguiente aproximación
        x1 = x0 - f_x0 / f_x0_prime

        # Cálculo del error relativo
        err = current_error(x1, x0)

        # Almacenar resultados en el diccionario
        resultados["x"].append(x1)
        resultados["f"].append(func(x1))
        resultados["e"].append(err)

        # Comprobar convergencia
        if err < tol:
            resultados["found"] = 1
            break
        elif i == niter - 1:
            resultados["found"] = 0

        # Actualizar valores para la siguiente iteración
        x0 = x1

    return resultados

# print(newton("x**3 + 4*(x**2) - 10", 2.0, 0.001, 100, 0))
