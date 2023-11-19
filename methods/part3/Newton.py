import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def newton_interpolation(x, y):
    n = len(x)
    x_sym = sp.symbols('x')
    coefficients = np.zeros(n)

    for i in range(n):
        coefficients[i] = y[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (x[i] - x[i - j])

    interpolating_poly = sum([coefficients[i] * sp.prod([x_sym - x[k] for k in range(i)]) for i in range(n)])
    simplified_poly = sp.simplify(interpolating_poly)

    return str(simplified_poly)

# # Datos de ejemplo
# x = np.array([2, 3, 5, 7, 8])
# y = np.array([0, 2, 5, 12, 21])

# # Crear el polinomio de Newton para la interpolación
# simplified_polynomial = newton_interpolation_polynomial(x, y)
# print("Polinomio de Newton simplificado:")
# print(simplified_polynomial)
 
# # Puntos para graficar el polinomio (opcional)
# x_vals = np.linspace(0, 4, 100)
# y_vals = [simplified_polynomial.subs('x', val) for val in x_vals]

# plt.figure(figsize=(8, 6))
# plt.plot(x_vals, y_vals, label='Polinomio de Newton', color='red')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Interpolación de Newton (Polinomio simplificado)')
# plt.grid(True)
# plt.show()
