import numpy as np
import sympy as sym

def spline(xi,fi):
    n = len(xi)
    x = sym.Symbol('x')
    px_tabla = []
    
    tramo = 1
    while not(tramo>=n):
        # con 1ra diferencia finita avanzada 
        numerador = fi[tramo]-fi[tramo-1]
        denominador = xi[tramo]-xi[tramo-1]
        m = numerador/denominador
        pxtramo = fi[tramo-1] + m*(x-xi[tramo-1])
        px_tabla.append(str(pxtramo))
        tramo = tramo + 1
        
    return(px_tabla)

# # PROGRAMA
# # INGRESO , Datos de prueba
# xi = [0.1 , 0.2, 0.3, 0.4]
# fi = [1.45, 1.8, 1.7, 2.0]
# muestras = 10 # entre cada par de puntos

# # PROCEDIMIENTO
# # Tabla de polinomios por tramos
# n = len(xi)
# px_tabla = trazalineal(xi,fi)

# # SALIDA
# print('Polinomios por tramos: ')
# for tramo in range(1,n,1):
#     print('  x = ['+str(xi[tramo-1])
#           +','+str(xi[tramo])+']')
#     print(str(px_tabla[tramo-1]))