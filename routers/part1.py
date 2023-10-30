from fastapi import APIRouter

router = APIRouter(prefix="/part1",tags=["part1"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 1"

@router.get("/biseccion")
async def biseccion():
    return "Metodo biseccion"

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