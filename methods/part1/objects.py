from pydantic import BaseModel

class Bisection(BaseModel):
    fun: str 
    a: float 
    b: float
    tol: float
    niter: int