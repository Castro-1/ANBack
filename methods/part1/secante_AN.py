import numpy as np
import matplotlib.pyplot as plt

def metodo_de_la_secante(func_str, x0, x1, tol, niter, error):
    # Convierte el string en una función ejecutable
    func = lambda x: eval(func_str)

    resultados = {
        "found": None,
        "iteracion": [],
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
        error = abs((x2 - x1) / x2)

        # Almacenar resultados en el diccionario
        resultados["iteracion"].append(i + 1)
        resultados["x"].append(x2)
        resultados["f"].append(func(x2))
        resultados["e"].append(error)

        # Comprobar convergencia
        if error < tol:
            resultados["found"] = 1
            break
        elif i == niter - 1:
            resultados["found"] = 0

        # Actualizar valores para la siguiente iteración
        x0 = x1
        x1 = x2

    for key in resultados:
        print(f"{key}: {resultados[key]}")

    # Gráfica de la función y las aproximaciones
    #x = np.linspace(0, 3, 400)
    #y = [func(val) for val in x]
    #plt.plot(x, y, label='f(x)')
    #plt.scatter(resultados["x"], resultados["f"], color='red', marker='o', label='Aproximaciones')
    #plt.xlabel('x')
    #plt.ylabel('f(x)')
    #plt.legend()
    #plt.title('Método de la Secante')
    #plt.grid()
    #plt.show()


metodo_de_la_secante("x**3 - 2*x**2 - 5", 1.0, 2.0, 1e-6, 100, 0)