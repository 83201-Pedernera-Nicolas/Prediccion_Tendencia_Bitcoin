from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import uvicorn
import pickle

app = FastAPI()

# Cargar el modelo y el scaler
model = tf.keras.models.load_model("btc_lstm_model.h5")
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Definir el esquema de entrada con Pydantic
class InputData(BaseModel):
    open: float
    high: float
    low: float
    close: float
    SMA_20: float
    SMA_50: float
    RSI_14: float
    BB_Upper: float
    BB_Lower: float
    volume: float

def preprocess_data(data):
    """Preprocesa los datos para que coincidan con la entrada del modelo LSTM."""
    df = pd.DataFrame([data.dict()])  # Convertir el diccionario en DataFrame
    df_scaled = scaler.transform(df)  # Normalizar con el scaler entrenado

    # Crear una secuencia de 20 pasos de tiempo duplicando los mismos valores
    df_sequence = np.tile(df_scaled, (20, 1))  # Repetir la misma fila 20 veces

    df_sequence = np.array(df_sequence).reshape(1, 20, len(df.columns))  # Ajustar forma para LSTM
    return df_sequence



@app.post("/predict/")
def predict(data: InputData):
    """Recibe datos y devuelve la predicción de tendencia"""
    try:
        print(f"Datos recibidos: {data}")  # Ver qué llega a la API
        X_input = preprocess_data(data)
        prediction = model.predict(X_input)
        result = int(prediction[0][0] > 0.5)
        return {"prediction": result}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

