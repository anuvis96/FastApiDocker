from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola Daniel esto es una prueba del composer con FastApi"}