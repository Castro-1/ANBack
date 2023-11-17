import numpy as np
from sympy import symbols, simplify

def divided_differences(x, y):
    n = len(x)
    coefficients = np.copy(y)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (x[i] - x[i - j])
    return coefficients

def newton_interpolation_polynomial(x, y):
    coefficients = divided_differences(x, y)
    n = len(x)
    x_sym = symbols('x')

    def newton_polynomial(new_x):
        result = coefficients[n - 1]
        for i in range(n - 2, -1, -1):
            result = result * (new_x - x[i]) + coefficients[i]
        return result

    newton_poly = newton_polynomial(x_sym)
    simplified_poly = simplify(newton_poly)

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
