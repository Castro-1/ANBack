from numpy.linalg import norm
import numpy as np

def current_error(x_new, x, orden, error):
        if error == 0:
            if orden == "inf":
                return norm(x_new - x, ord=np.inf)
            else:
                return norm(x_new - x, ord=int(orden))
        else:
            if orden == "inf":
                return norm(x_new - x, ord=np.inf) / norm(x_new, ord=np.inf)
            else:
                return norm(x_new - x, ord=int(orden)) / norm(x_new, ord=int(orden))