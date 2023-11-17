from fastapi import FastAPI
from routers import part1, part2, part3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(part1.router)
app.include_router(part2.router)
app.include_router(part3.router)

origins = [
    "http://127.0.0.1:5173/parte1/biseccion"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return "Hello, base path"