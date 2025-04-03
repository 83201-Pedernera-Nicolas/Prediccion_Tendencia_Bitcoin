from binance.client import Client
import pandas as pd
import datetime

# Claves de API (Si necesitas autenticación para datos avanzados)
API_KEY = "tu_api_key"
API_SECRET = "tu_api_secret"

# Conectar con la API de Binance
# client = Client(API_KEY, API_SECRET)
client = Client()

# Definir el par de trading y el intervalo de tiempo
symbol = "BTCUSDT"  # Bitcoin contra USDT
timeframe = Client.KLINE_INTERVAL_1DAY  # Datos diarios

# Rango de fechas para extraer datos
start_date = "2023-01-01"
end_date = "2025-03-20"

# Convertir fechas a timestamp
start_timestamp = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp() * 1000)
end_timestamp = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp() * 1000)

# Obtener datos históricos
klines = client.get_historical_klines(symbol, timeframe, start_timestamp, end_timestamp)

# Convertir a DataFrame
df = pd.DataFrame(klines, columns=["timestamp", "open", "high", "low", "close", "volume", 
                                   "close_time", "quote_asset_volume", "number_of_trades", 
                                   "taker_buy_base", "taker_buy_quote", "ignore"])

# Convertir timestamp a fecha
df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')

# Convertir columnas numéricas
df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

# Guardar en CSV
df.to_csv("btc_data.csv", index=False)

# Mostrar las primeras filas
print(df.head())
