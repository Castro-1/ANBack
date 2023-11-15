import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify

def lagrange_interpolation_polynomial(x, y):
    x_sym = symbols('x')
    lagrange_poly = 0

    for i in range(len(x)):
        term = 1
        for j in range(len(x)):
            if i != j:
                term *= (x_sym - x[j]) / (x[i] - x[j])
        lagrange_poly += term * y[i]

    return str(simplify(lagrange_poly))

# # Datos de ejemplo
# x = np.array([0, 1, 2, 3, 4])
# y = np.array([0, 1, 4, 10 , 16])

# # Crear el polinomio de Lagrange para la interpolación
# polynomial = lagrange_interpolation_polynomial(x, y)
# simplified_poly = simplify(polynomial)

# # Mostrar el polinomio simplificado
# print("Polinomio de Lagrange simplificado:")
# print(simplified_poly)

# # Graficar el polinomio (opcional)
# x_vals = np.linspace(0, 4, 100)
# y_vals = [simplified_poly.subs('x', val) for val in x_vals]

# plt.figure(figsize=(8, 6))
# plt.plot(x_vals, y_vals, label='Polinomio de Lagrange', color='red')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Interpolación de Lagrange (Polinomio simplificado)')
# plt.grid(True)
# plt.show()
