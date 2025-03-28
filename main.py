
# app = FastAPI()

# app.include_router(router)

# @app.get("/")
# def read_root():
#     return {"mensaje": "¡Bienvenido a mi API FastAPI en Linux Mint!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar el directorio de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar el motor de plantillas Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predecir/", response_class=HTMLResponse)
async def predecir(request: Request, texto: str = Form(...)):
    from app.router import predecir_sentimiento
    resultado = await predecir_sentimiento(texto)
    return templates.TemplateResponse("formulario.html", {"request": request, "resultado": resultado})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)