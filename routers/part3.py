from fastapi import APIRouter
from routers.features import BaseInterpolation, convertInterpolationArrays, parsePoly
from methods.part3.Vandermonde import vandermonde
from methods.part3.Lagrange import lagrange_interpolation_polynomial
from methods.part3.Newton import newton_interpolation
from methods.part3.Spline import spline
from methods.part3.Spline3 import spline3


router = APIRouter(prefix="/part3",tags=["part3"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 3"

@router.post("/vandermonde")
async def method(params: BaseInterpolation):
    x,y = convertInterpolationArrays(params.x, params.y)
    poly = vandermonde(x,y)
    return parsePoly(poly)

@router.post("/newton")
async def method(params: BaseInterpolation):
    x,y = convertInterpolationArrays(params.x, params.y)
    poly = newton_interpolation(x,y)
    return parsePoly(poly)

@router.post("/lagrange")
async def method(params: BaseInterpolation):
    x, y = convertInterpolationArrays(params.x, params.y)
    poly = lagrange_interpolation_polynomial(x,y)
    return parsePoly(poly)

@router.post("/spline")
async def method(params: BaseInterpolation):
    x, y = convertInterpolationArrays(params.x, params.y)
    polys = spline(x,y)
    polys = [parsePoly(poly) for poly in polys]
    return polys

@router.post("/spline3")
async def method(params: BaseInterpolation):
    x, y = convertInterpolationArrays(params.x, params.y)
    polys = spline3(x,y)
    polys = [parsePoly(poly) for poly in polys]
    return polys