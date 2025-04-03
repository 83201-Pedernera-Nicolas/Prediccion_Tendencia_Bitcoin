import streamlit as st
import requests
import json

def main():
    st.title("Predicción de Tendencia de Bitcoin")
    st.write("Ingrese los datos para obtener la predicción de la tendencia del precio de Bitcoin.")
    
    # Campos de entrada para los datos
    open_price = st.number_input("Open Price", value=44000.5)
    high_price = st.number_input("High Price", value=44500.2)
    low_price = st.number_input("Low Price", value=43800.1)
    close_price = st.number_input("Close Price", value=44200.3)
    sma_20 = st.number_input("SMA 20", value=44150.6)
    sma_50 = st.number_input("SMA 50", value=43980.2)
    rsi_14 = st.number_input("RSI 14", value=55.2)
    bb_upper = st.number_input("BB Upper", value=45000.0)
    bb_lower = st.number_input("BB Lower", value=43000.0)
    volume = st.number_input("Volume", value=35000)
    
    # Botón para predecir
    if st.button("Predecir Tendencia"):
        input_data = {
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "close": close_price,
            "SMA_20": sma_20,
            "SMA_50": sma_50,
            "RSI_14": rsi_14,
            "BB_Upper": bb_upper,
            "BB_Lower": bb_lower,
            "volume": volume
        }
        
        # Llamada a la API de FastAPI
        api_url = "http://127.0.0.1:8000/predict/"
        response = requests.post(api_url, json=input_data)
        
        if response.status_code == 200:
            #st.write("Respuesta de la API:", response.json())  # Para ver qué devuelve la API
            prediction = response.json()["prediction"]
            result = "Subirá 📈" if prediction == 1 else "Bajará 📉"
            st.success(f"Predicción: {result}")
        else:
            st.error("Error al obtener la predicción. Verifica la API.")

if __name__ == "__main__":
    main()
