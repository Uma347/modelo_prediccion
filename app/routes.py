from fastapi import APIRouter
import joblib

router = APIRouter()

# Cargar el modelo entrenado
modelo = joblib.load("app/ml/sentiment_model.pkl")

@router.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}

@router.post("/predecir/")
def predecir_sentimiento(texto: str):
    resultado = modelo.predict([texto])[0]
    sentimiento = "Positivo" if resultado == 1 else "Negativo"
    return {"texto": texto, "sentimiento": sentimiento}
