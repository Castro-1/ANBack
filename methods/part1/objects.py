from pydantic import BaseModel

class Bisection(BaseModel):
    fun: str 
    a: int 
    b: int
    tol: float
    niter: int