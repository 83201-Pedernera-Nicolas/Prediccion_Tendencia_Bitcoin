# import pandas as pd
# import pickle
# from sklearn.preprocessing import StandardScaler

# # Cargar los datos
# df = pd.read_csv("btc_features.csv")

# # Seleccionar las mismas características usadas en el modelo
# features = ["open", "high", "low", "close", "SMA_20", "SMA_50", "RSI_14", "BB_Upper", "BB_Lower", "volume"]
# X = df[features]

# # Crear y entrenar el scaler
# scaler = StandardScaler()
# scaler.fit(X)  # Ajustamos el scaler a los datos originales

# # Guardar el scaler correctamente
# with open("scaler.pkl", "wb") as f:
#     pickle.dump(scaler, f)

# print("Scaler guardado correctamente en scaler.pkl")

import pickle

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

print(type(scaler))  # Debe imprimir <class 'sklearn.preprocessing._data.StandardScaler'>

