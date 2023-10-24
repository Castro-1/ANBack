import numpy as np

def doolittle_factorization(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Calcula la parte superior de la matriz U
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        # Calcula la parte inferior de la matriz L
        L[i][i] = 1  # La diagonal de L es 1
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

# Ejemplo de uso:
if __name__ == "__main__":
    # Reemplaza esta matriz A con tu propia matriz.
    A = np.array([[36., 3., -44., 5.],
                  [-5., -45., 10., -21.],
                  [6., 82., 57., 5.],
                  [12., 3., -8., -42.]])

    L, U = doolittle_factorization(A)
    print("Matriz L:")
    print(L)
    print("Matriz U:")
    print(U)