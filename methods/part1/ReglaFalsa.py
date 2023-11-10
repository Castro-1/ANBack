def regla_falsa(func_str, a, b, tol, niter, error):
    def current_error(x2, x1):
        if error == 0:
            return abs(x2 - x1)
        else:
            return abs(x2 - x1) / x2

    # Convierte el string en una función ejecutable
    func = lambda x: eval(func_str)

    resultados = {
        "found": None,
        "x": [],
        "f": [],
        "e": []
    }

    for i in range(niter):
        f_a = func(a)
        f_b = func(b)

        # Cálculo de la siguiente aproximación usando regla falsa
        c = b - (f_b * (b - a)) / (f_b - f_a)

        # Cálculo del error relativo
        err = current_error(c, b)

        # Almacenar resultados en el diccionario
        resultados["x"].append(c)
        resultados["f"].append(func(c))
        resultados["e"].append(err)

        # Comprobar convergencia
        if err < tol:
            resultados["found"] = 1
            break
        elif i == niter - 1:
            resultados["found"] = 0

        # Actualizar valores para la siguiente iteración
        if func(c) * f_b < 0:
            a = c
        else:
            b = c

    return resultados


# regla_falsa("x**3 - 2*x**2 - 5", 1.0, 2.0, 1e-6, 100, 0)