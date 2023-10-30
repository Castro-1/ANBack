from fastapi import APIRouter

router = APIRouter(prefix="/part1",tags=["part1"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 1"

@router.get("/puntofijo")
async def puntoFijo():
    return "Metodo punto fijo"