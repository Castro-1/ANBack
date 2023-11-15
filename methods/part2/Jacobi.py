import numpy as np
from numpy.linalg import norm

def jacobi_method(A, b, x0, tol, max_iter, error):
    D = np.diag(np.diag(A))
    X = []
    LU = A - D
    x = x0
    convergence = 0
    for i in range(max_iter):
        x_new = np.dot(np.linalg.inv(D), b - np.dot(LU, x))
        if norm(x - x_new,np.inf) < tol:
            convergence = 1
            break
        x = x_new
        X.append(x)

    return X, x, convergence

def spectral_radius(A):
    eigenvalues, _ = np.linalg.eig(A)
    return max(abs(eigenvalues))

def solve_jacobi(A, b, x0, tol, max_iter, error):
    spectral_r = spectral_radius(A)
    x_values, sol, convergence = jacobi_method(A, b, x0, tol, max_iter, error)
    sol = sol.tolist()
    x_values = [x.tolist() for x in x_values]
    return {"radio": spectral_r, "converge": convergence, "sol": sol, "x": x_values}


# print(solve_jacobi(np.array([[6, 5, 6], [-2, 5, 1], [-1, -1, 4]]), np.array([15, 15, 20]), np.array([1, 1, 1]),0.1,1000 ))