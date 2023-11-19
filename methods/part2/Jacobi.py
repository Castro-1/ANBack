import numpy as np
from methods.part2.features import current_error

def jacobi_method(A, b, x0, tol, orden, max_iter, error):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x0
    convergence = 0
    x_list = [x]
    n_iter = []
    

    for i in range(max_iter):
        x_new = np.dot(np.linalg.inv(D), b - np.dot(LU, x))
        x_list.append(x_new)
        n_iter.append(i + 1)
        err = current_error(x_new, x, orden, error)
        
        if err < tol:
            convergence = 1
            break
        x = x_new

    return x, convergence, n_iter, x_list

def spectral_radius(T):
    eigenvalues, _ = np.linalg.eig(T)
    return max(abs(eigenvalues))

def solve_jacobi(A, b, x0, tol, orden, max_iter, error):
    D = np.diag(np.diag(A))
    LU = A - D
    T = np.dot(np.linalg.inv(D), LU)
    
    sol, convergence, n_iter, x_values = jacobi_method(A, b, x0, tol, orden, max_iter, error)
    spectral_r = spectral_radius(T)

    sol = sol.tolist()
    x_values = [x.tolist() for x in x_values]
    T = [T.tolist() for t in T]
    
    return {"radio": spectral_r, "converge": convergence, "sol": sol, "niter": n_iter, "x": x_values, "T":T}

# Ejemplo de uso con error relativo (error=1) y tolerancia 1e-10
# print(solve_jacobi(np.array([[5, 1, 2], [1, 5, 1], [2, 1, 5]]), np.array([6, 6, 6]), np.array([0, 0, 0]), 1e-10, "1", 1000, 0))