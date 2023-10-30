from fastapi import FastAPI
from routers import part1, part2, part3

app = FastAPI()

app.include_router(part1.router)
app.include_router(part2.router)
app.include_router(part3.router)

@app.get("/")
async def root():
    return "Hello, base path"