from fastapi import APIRouter

router = APIRouter(prefix="/part2",tags=["part2"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 2"

@router.get("/jacobi")
async def method():
    return "Metodo jacobi"

@router.get("/gauss-seidel")
async def method():
    return "Metodo gauss seidel"

@router.get("/sor")
async def method():
    return "Metodo sor"