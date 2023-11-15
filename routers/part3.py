from fastapi import APIRouter
from routers.features import BaseInterpolation, convertInterpolationArrays, parsePoly
from methods.part3.Lagrange import lagrange_interpolation_polynomial
from methods.part3.Newton import newton_interpolation_polynomial


router = APIRouter(prefix="/part3",tags=["part3"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 3"

@router.post("/vandermonde")
async def method():
    return "Metodo vandermonde"

@router.post("/newton")
async def method(params: BaseInterpolation):
    x,y = convertInterpolationArrays(params.x, params.y)
    poly = newton_interpolation_polynomial(x,y)
    return parsePoly(poly)

@router.post("/lagrange")
async def method(params: BaseInterpolation):
    x, y = convertInterpolationArrays(params.x, params.y)
    poly = lagrange_interpolation_polynomial(x,y)
    return parsePoly(poly)

@router.post("/spline")
async def method():
    return "Metodo spline"