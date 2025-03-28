from fastapi import FastAPI
from app import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a mi API FastAPI en Linux Mint!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
