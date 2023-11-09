from fastapi import APIRouter
from routers.features import IntervalInput, FixedPoint, Newton, format_function
from methods.part1.Biseccion import biseccion
from methods.part1.Secante import secante
from methods.part1.Newton import newton
from methods.part1.PuntoFijo import punto_fijo
from methods.part1.RaicesMultiples import newton_raices_multiples

router = APIRouter(prefix="/part1",tags=["part1"],responses={404:{"message":"Metodo no encontrado."}})

@router.post("/")
async def root():
    return "Bienvenido a parte 1"

@router.post("/biseccion")
async def method(params: IntervalInput):
    fun, a, b, tol, niter, error = params.fun, params.a, params.b, params.tol, params.niter, params.error
    fun = format_function(fun)
    return biseccion(fun,a,b,tol,niter,error)

@router.post("/reglafalsa")
async def method(params: IntervalInput):
    fun, a, b, tol, niter, error = params.fun, params.a, params.b, params.tol, params.niter, params.error
    return "Metodo regla falsa"

@router.post("/puntofijo")
async def method(params: FixedPoint):
    fun, dfun, x0, tol, niter, error = params.fun, params.dfun, params.x0, params.tol, params.niter, params.error
    fun = format_function(fun)
    dfun = format_function(dfun)
    return punto_fijo(fun, dfun, x0, tol, niter, error)

@router.post("/newton")
async def method(params: Newton):
    fun, x, tol, niter, error = params.fun, params.x, params.tol, params.niter, params.error
    fun = format_function(fun)
    return newton(fun, x, tol, niter, error)

@router.post("/secante")
async def method(params: IntervalInput):
    fun, a, b, tol, niter, error = params.fun, params.a, params.b, params.tol, params.niter, params.error
    fun = format_function(fun)
    return secante(fun, a, b, tol, niter, error)

@router.post("/raicesmultiples")
async def method(params: Newton):
    fun, x, tol, niter, error = params.fun, params.x, params.tol, params.niter, params.error
    fun = format_function(fun)
    return newton_raices_multiples(fun, x, tol, niter, error)