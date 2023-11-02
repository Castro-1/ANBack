from fastapi import APIRouter

router = APIRouter(prefix="/part3",tags=["part3"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 3"

@router.get("/vandermonde")
async def method():
    return "Metodo vandermonde"

@router.get("/newton")
async def method():
    return "Metodo newton"

@router.get("/lagrange")
async def method():
    return "Metodo lagrange"

@router.get("/spline")
async def method():
    return "Metodo spline"