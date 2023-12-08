import sympy as sp
from methods.part1.features import current_error
import math
import numpy as np

def newton_raices_multiples(func_str, x0, tol, niter, error):
    x = sp.Symbol('x')
    func = sp.sympify(func_str)
    print(func)
    func_prime = sp.diff(func, x)

    resultados = {
        "found": None,
        "x": [],
        "f": [],
        "e": []
    }

    for i in range(niter):
        f_x0 = func.subs(x, x0)
        if abs(f_x0) < 1e-12:
            resultados["found"] = 1
            break

        f_x0_prime = func_prime.subs(x, x0)
        if abs(f_x0_prime) < 1e-12:
            resultados["found"] = 0
            break

        x1 = x0 - f_x0 / f_x0_prime

        err = current_error(x1, x0, error)

        resultados["x"].append(float(x1))
        resultados["f"].append(float(func.subs(x, x1)))
        resultados["e"].append(float(err))

        if err < tol:
            resultados["found"] = 1
            break
        elif i == niter - 1:
            resultados["found"] = 0

        x0 = x1

    return resultados

# print(newton_raices_multiples("x**4 - 8*x**3 + 21*x**2 - 18*x", -1, 0.001, 100, 0))