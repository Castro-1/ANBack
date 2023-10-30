from fastapi import FastAPI
from routers import part1

app = FastAPI()

app.include_router(part1.router)

@app.get("/")
async def root():
    return "Hello, base path"