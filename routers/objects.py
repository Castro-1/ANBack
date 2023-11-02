from pydantic import BaseModel

class BaseInput(BaseModel):
    fun: str 
    tol: float
    niter: int
    error: int

class IntervalInput(BaseInput):
    a: float 
    b: float

class FixedPoint(IntervalInput):
    dfun: str

class Newton(BaseInput):
    dfun: str
    x: float