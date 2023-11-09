import math
import sympy as sp
import matplotlib.pyplot as plt

def newton_raices_multiples(func_str, x0, tol, niter, error):
    x = sp.Symbol('x')
    func = sp.sympify(func_str)
    func_prime = sp.diff(func, x)

    def current_error(x1, x0):
        if error == 0:
            return abs(x1 - x0)
        else:
            return abs(x1 - x0) / abs(x1)

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

        err = current_error(x1, x0)

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

newton_raices_multiples("x**3 - 2*x**2 - 5", 1.0, 1e-6, 100, 0)