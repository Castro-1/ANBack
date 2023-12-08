import re
import numpy as np
from pydantic import BaseModel


# Parte 1
def add_asterisk(match):
    return match.group(1) + '*' + match.group(2)


def format_function(fun):
    fun = re.sub(r'(\d)(x)', add_asterisk, fun)
    fun = re.sub(r'\^', '**', fun)
    fun = re.sub(r'\blog\b', 'np.log', fun)
    fun = re.sub(r'\bln\b', 'np.log', fun)
    fun = re.sub(r'\bexp\b', 'np.exp', fun)
    fun = re.sub(r'\btan\b', 'np.tan', fun)
    fun = re.sub(r'\bsin\b', 'np.sin', fun)
    fun = re.sub(r'\bcos\b', 'np.cos', fun)
    # print(fun)
    return fun


class BaseInput(BaseModel):
    fun: str 
    tol: float
    niter: int
    error: int

class IntervalInput(BaseInput):
    a: float 
    b: float

class Newton(BaseInput):
    x0: float

class FixedPoint(Newton):
    dfun: str

# Parte 2
def convertArrays(A,b,x0):
    A = np.array(A)
    b = np.array(b)
    x0 = np.array(x0)
    return A, b, x0

class BaseMatrixInput(BaseModel):
    A: list
    b: list
    x0: list
    tol: float
    norm: str
    niter: int
    error: int

class SORInput(BaseMatrixInput):
    omega: float

# Parte 3
def convertInterpolationArrays(x,y):
    x = np.array(x)
    y = np.array(y)
    return x, y

def parsePoly(poly):
    poly = re.sub(r'\*\*', '^', poly)
    return poly

class BaseInterpolation(BaseModel):
    x: list
    y: list
