import numpy as np
#import matplotlib.pyplot as plt

# MÉTODO DE LA SECANTE

# Función para la que se busca la raíz
def f(x):
    return x**3 - 2*x**2 - 5

# Datos de prueba
x0 = 1.0  # Valor inicial x0
x1 = 2.0  # Valor inicial x1
tolerancia = 1e-6  # Tolerancia para la convergencia
max_iter = 100  # Máximo número de iteraciones

# Diccionario para almacenar resultados
resultados = {
    "found": None,
    "iteracion": [],
    "x de la iteración": [],
    "f(x)": [],
    "e": [] }

# Método de la secante
for i in range(max_iter):
    # Cálculo de la siguiente aproximación
    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

    # Cálculo del error relativo
    error = abs((x2 - x1) / x2)

    # Almacenar resultados en el diccionario
    resultados["iteracion"].append(i + 1)
    resultados["x de la iteración"].append(x2)
    resultados["f(x)"].append(f(x2))
    resultados["e"].append(error)

    # Comprobar convergencia
    if error < tolerancia:
        resultados["found"] = 1
        break
    elif i == max_iter - 1:
        resultados["found"] = 0

    # Actualizar valores para la siguiente iteración
    x0 = x1
    x1 = x2



for key in resultados:
    print(f"{key}: {resultados[key]}")

# Gráfica de la función y las aproximaciones
#x = np.linspace(0, 3, 400)
#y = f(x)
#print(resultados)
#plt.plot(x, y, label='f(x)')
#plt.scatter(resultados["x de la iteración"], resultados["f(x)"], color='red', marker='o', label='Aproximaciones')
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.legend()
#plt.title('Método de la Secante')
#plt.grid()
#plt.show()