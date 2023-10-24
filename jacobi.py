import numpy as np

# CALCULAR RADIO ESPECTRAL
def spectral_radius(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    return max(abs(eigenvalues))

# CALCULAR MATRIZ T
def jacobi_T_matrix(A):
    n = A.shape[0]
    T = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                T[i][j] = -A[i][j] / A[i][i]
    
    return T

def jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for iteration in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            sum_Ax = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_Ax) / A[i, i]
        if np.linalg.norm(x - x_new) < tol:
            return x_new
        x = x_new
    raise Exception("El método de Jacobi no convergió después de {} iteraciones".format(max_iter))

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la matriz de coeficientes A
    A = np.array([[4, -1, 0],
                 [-1, 4, -1],
                 [0, -1, 3]])

    # Definir el vector de términos constantes b
    b = np.array([1, 2, 0])

    # Definir la aproximación inicial x0
    x0 = np.array([0, 0, 0])

    # Definir la tolerancia y el número máximo de iteraciones
    tol = 1e-6
    max_iter = 1000

    # Matiz T
    T = jacobi_T_matrix(A)

    # Radio espectral
    print("Radio espectral: ", spectral_radius(T))

    # Aplicar el método de Jacobi
    solution = jacobi(A, b, x0, tol, max_iter)
    print("Solución encontrada:")
    print(solution)
