from fastapi import APIRouter
from routers.features import convertArrays, BaseMatrixInput, SORInput
from methods.part2.GaussSeidel import solve_gauss_seidel
from methods.part2.Jacobi import solve_jacobi
from methods.part2.SOR import solve_sor

router = APIRouter(prefix="/part2",tags=["part2"],responses={404:{"message":"Metodo no encontrado."}})

@router.get("/")
async def root():
    return "Bienvenido a parte 2"

@router.post("/jacobi")
async def method(params: BaseMatrixInput):
    A, b, x0, tol, orden, niter, error = params.A, params.b, params.x0, params.tol, params.norm, params.niter, params.error
    A, b, x0 = convertArrays(A, b, x0)
    return solve_jacobi(A, b, x0, tol, orden, niter, error)

@router.post("/gaussseidel")
async def method(params: BaseMatrixInput):
    A, b, x0, tol, orden, niter, error = params.A, params.b, params.x0, params.tol, params.norm, params.niter, params.error
    A, b, x0 = convertArrays(A, b, x0)
    return solve_gauss_seidel(A, b, x0, tol, orden, niter, error)

@router.post("/sor")
async def method(params: SORInput):
    A, b, x0, omega, tol, orden, niter, error = params.A, params.b, params.x0, params.omega, params.tol, params.norm, params.niter, params.error
    A, b, x0 = convertArrays(A, b, x0)
    return solve_sor(A, b, x0, omega, tol, orden, niter, error)