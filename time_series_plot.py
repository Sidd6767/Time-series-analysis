import pandas as pd
import matplotlib.pyplot as plt
import requests

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
data = pd.read_csv(url)

data['Date'] = pd.to_datetime(data['Date'])

plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Temp'], label='Daily Min Temperature', color='red')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Minimum Temperatures Over Time")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()

data.to_csv("daily_min_temperatures.csv", index=False)
