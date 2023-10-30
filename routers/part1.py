import re
from fastapi import APIRouter
from methods.part1.objects import Bisection
from methods.part1.Biseccion import biseccion

router = APIRouter(prefix="/part1",tags=["part1"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 1"

@router.post("/biseccion")
async def method(params: Bisection):
    fun, a, b, tol, niter = params.fun, params.a, params.b, params.tol, params.niter
    fun = re.sub(r'\^', '**', fun)
    return biseccion(fun,a,b,tol,niter)

@router.get("/reglafalsa")
async def reglaFalsa():
    return "Metodo regla falsa"

@router.get("/puntofijo")
async def puntoFijo():
    return "Metodo punto fijo"

@router.get("/newton")
async def newton():
    return "Metodo newton"

@router.get("/secante")
async def secante():
    return "Metodo secante"

@router.get("/raicesmultiples")
async def raicesMultiples():
    return "Metodo raices multiples"