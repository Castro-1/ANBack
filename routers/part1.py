import re
from fastapi import APIRouter
from routers.objects import IntervalInput, FixedPoint, Newton
from methods.part1.Biseccion import biseccion

router = APIRouter(prefix="/part1",tags=["part1"],responses={404:{"message":"Metodo no encontrado."}})

@router.post("/")
async def root():
    return "Bienvenido a parte 1"

@router.post("/biseccion")
async def method(params: IntervalInput):
    fun, a, b, tol, niter, error = params.fun, params.a, params.b, params.tol, params.niter, params.error
    fun = re.sub(r'\^', '**', fun)
    fun = re.sub(r'\blog\b', 'math.log10', fun)
    fun = re.sub(r'\bln\b', 'math.log', fun)
    print(fun)
    return biseccion(fun,a,b,tol,niter,error)

@router.post("/reglafalsa")
async def method(params: IntervalInput):
    fun, a, b, tol, niter, error = params.fun, params.a, params.b, params.tol, params.niter, params.error
    return "Metodo regla falsa"

@router.post("/puntofijo")
async def method(params: FixedPoint):
    fun, dfun, a, b, tol, niter, error = params.fun, params.dfun, params.a, params.b, params.tol, params.niter, params.error
    return "Metodo punto fijo"

@router.post("/newton")
async def method(params: Newton):
    fun, dfun, x, tol, niter, error = params.fun, params.dfun, params.x, params.tol, params.niter, params.error
    return "Metodo newton"

@router.post("/secante")
async def method(params: IntervalInput):
    fun, a, b, tol, niter, error = params.fun, params.a, params.b, params.tol, params.niter, params.error
    return "Metodo secante"

@router.post("/raicesmultiples")
async def method():
    return "Metodo raices multiples"