import numpy as np
from numpy.linalg import norm

def gauss_seidel_method(A, b, x0, tol, max_iter, error):
    L = np.tril(A)
    U = A - L
    x = x0
    convergence = 0
    x_list = [x]
    n_iter = []
    for i in range(max_iter):
        x_new = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        x_list.append(x_new)
        n_iter.append(i + 1)
        if norm(x - x_new) < tol:
            convergence = 1
            break
        x = x_new
    return x, convergence, n_iter, x_list

def spectral_radius(A):
    eigenvalues, _ = np.linalg.eig(A)
    return max(abs(eigenvalues))

def solve_gauss_seidel(A, b, x0, tol, max_iter, error):
    spectral_r = spectral_radius(A)
    sol, convergence, n_iter, x_values = gauss_seidel_method(A, b, x0, tol, max_iter)
    sol = sol.tolist()
    x_values = [x.tolist() for x in x_values]
    return {"radio": spectral_r, "converge": convergence, "sol": sol, "niter": n_iter, "x": x_values}

# solve_gauss_seidel(np.array([[5, 1, 0], [1, 5, 1], [0, 1, 5]]), np.array([6, 6, 6]), np.array([0, 0, 0]), 1e-10, 1000)