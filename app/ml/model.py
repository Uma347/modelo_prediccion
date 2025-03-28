import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Datos de entrenamiento (frases con sentimiento)
data = {
    "texto": [
        "Me encanta este producto",
        "Odio este servicio",
        "Es lo mejor que he comprado",
        "No me gustó para nada",
        "Estoy muy feliz con el resultado",
        "Es una completa estafa"
    ],
    "sentimiento": [1, 0, 1, 0, 1, 0]  # 1 = positivo, 0 = negativo
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Crear pipeline de procesamiento y modelo
modelo = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Entrenar el modelo
modelo.fit(df["texto"], df["sentimiento"])

# Guardar el modelo entrenado
joblib.dump(modelo, "ml/sentiment_model.pkl")

print("✅ Modelo de IA entrenado y guardado en 'ml/sentiment_model.pkl'")
