# Método de Gauss-Seidel
# solución de sistemas de ecuaciones
# por métodos iterativos

import numpy as np

# CALCULAR MATRIZ T
def T_matrix(A):
    n = A.shape[0]
    T_G = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i == j:
                T_G[i][j] = 0
            else:
                T_G[i][j] = -A[i][j] / A[i][i]
    
    return T_G

# CALCULAR RADIO ESPECTRAL
def spectral_radius(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    return max(abs(eigenvalues))

# INGRESO
A = np.array([[3. , -5., -8.],
              [2.,  4.  , 6.],
              [3., 4., -12.  ]])

B = np.array([-15.,12,8])

X0  = np.array([1.,1,1])

tolera = 5E-5
iteramax = 100

# PROCEDIMIENTO

# Gauss-Seidel
tamano = np.shape(A)
n = tamano[0]
m = tamano[1]
#  valores iniciales
X = np.copy(X0)
diferencia = np.ones(n, dtype=float)
errado = 2*tolera

itera = 0
while not(errado<=tolera or itera>iteramax):
    # por fila
    for i in range(0,n,1):
        # por columna
        suma = 0 
        for j in range(0,m,1):
            # excepto diagonal de A
            if (i!=j): 
                suma = suma-A[i,j]*X[j]
        
        nuevo = (B[i]+suma)/A[i,i]
        diferencia[i] = np.abs(nuevo-X[i])
        X[i] = nuevo
    errado = np.max(diferencia)
    itera = itera + 1

# Respuesta X en columna
X = np.transpose([X])

# revisa si NO converge
if (itera>iteramax):
    X=0
# revisa respuesta
verifica = np.dot(A,X)

# Matriz T
T = T_matrix(A)

# Radio Espectral
print("Radio espectral: ",spectral_radius(T))

# SALIDA
print('respuesta X: ')
print(X)
print('verificar A.X=B: ')
print(verifica)