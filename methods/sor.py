import numpy as np
from numpy.linalg import norm

def sor_method(A, b, x0, omega, tol, max_iter):
    L = np.tril(A)
    U = A - L
    x = x0
    convergence = 0
    x_list = [x]
    n_iter = []
    for i in range(max_iter):
        x_new = np.dot(np.linalg.inv(L + omega * np.diag(np.diag(A))), 
                       (b - np.dot(U, x)))       
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

def solve_sor(A, b, x0, omega, tol, max_iter):
    spectral_r = spectral_radius(A)
    sol, convergence, n_iter, x_values = sor_method(A, b, x0, omega, tol, max_iter)
    return {"radio": spectral_r, "converge": convergence, "sol": sol, "niter": n_iter, "x": x_values}

solve_sor(np.array([[5, 1, 0], [1, 5, 1], [0, 1, 5]]), np.array([6, 6, 6]), np.array([0, 0, 0]), 1.1, 1e-10, 1000)