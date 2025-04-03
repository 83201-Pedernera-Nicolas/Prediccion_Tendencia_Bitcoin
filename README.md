# 📈 Predicción de Tendencia de Bitcoin con LSTM & Random Forest

Este proyecto implementa un modelo de predicción de la tendencia del precio de Bitcoin usando **redes neuronales LSTM** y **Random Forest**. La API en **FastAPI** expone el modelo y un **dashboard en Streamlit** permite la interacción con el usuario.

## 🚀 Tecnologías utilizadas
- Python
- FastAPI (para la API)
- TensorFlow (para el modelo LSTM)
- Scikit-Learn (para Random Forest y preprocesamiento)
- Streamlit (para el dashboard interactivo)
- Pandas y NumPy (para el manejo de datos)
- Uvicorn (para correr el servidor)

---

## 📡 API en FastAPI

### 📌 **Cómo ejecutar la API**
1. Instalar dependencias:
   ```bash
   cd api
   pip install -r requirements.txt
2. Correr el servidor:
   ```bash
   uvicorn api_btc:app --reload
3. La API estará disponible en http://127.0.0.1:8000
### 🔥 **Ejemplo de consulta en Postman o curl**
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{
  "open": 44000.5,
  "high": 44500.2,
  "low": 43800.1,
  "close": 44200.3,
  "SMA_20": 44150.6,
  "SMA_50": 43980.2,
  "RSI_14": 55.2,
  "BB_Upper": 45000.0,
  "BB_Lower": 43000.0,
  "volume": 35000
}'

## 📊 Dashboard en Streamlit

### 📌 **Cómo ejecutar el dashboard**
1. Instalar dependencias:
   ```bash
   cd dashboard
   pip install -r requirements.txt
2. Ejecutar el dashboard:
   ```bash
   streamlit run dashboard.py
3. Abrir http://localhost:8501 en el navegador.

## 📔 Notebooks de entrenamiento y análisis
En la carpeta `notebooks/` encontrarás los Jupyter Notebooks con todo el proceso de análisis y modelado:

1. **Exploración de Datos** (`analisis.ipynb`)  
   📊 Análisis inicial de los datos, generación de gráficos y limpieza.  
2. **Modelos** (`modelos_prediccion_btc.ipynb`)  
   🤖 Creación y entrenamiento modelos de entrenamiento Random Forest y red neuronal LSTM para predicción de tendencias. Comparacion de metricas y seleccion del mejor modelo. 

## 📁 Estructura del proyecto
📦 Prediccion_Bitcoin
┣ 📂 api                  # Carpeta para la API en FastAPI
┃ ┣ 📜 API_btc_prediccion.py         # Código de la API
┃ ┣ 📜 btc_lstm_model.h5  # Modelo LSTM guardado
┃ ┣ 📜 scaler.pkl         # Scaler guardado
┃ ┣ 📜 requirements.txt   # Librerías necesarias
┣ 📂 dashboard            # Carpeta para el dashboard en Streamlit
┃ ┣ 📜 dashboard_streamlit.py       # Código de Streamlit
┃ ┣ 📜 requirements.txt   # Librerías necesarias para Streamlit
┣ 📂 notebooks            # Carpeta con los Jupyter Notebooks de entrenamiento
┃ ┣ 📜 analisis.ipynb       # Análisis exploratorio de los datos
┃ ┣ 📜 modelos_prediccion_btc.ipynb      # Entrenamiento del modelo Random Forest y LSTM y comparación de los mismos
┣ 📂 data                 # Datos utilizados (opcional, solo si compartes muestras)
┃ ┣ 📜 datos_binance.py   # Script para obtener los datos de la API de Binance
┃ ┣ 📜 btc_data.csv   # Dataset original obtenido de la API de Binance
┃ ┣ 📜 btc_data_features.csv   # Dataset con features generados en entrenamiento de modelos
┃ ┗ 📜 btc_features.csv   # Dataset con features (sin datos sensibles)
┣ 📜 .gitignore           # Archivos a ignorar en Git
┗ 📜 README.md            # Explicación general del proyecto


