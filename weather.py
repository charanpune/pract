import random

def generate_weather_data(days=7):
    weather = []
    for day in range(1, days+1):
        temp = random.randint(20, 40)  # Celsius
        humidity = random.randint(30, 90)  # %
        weather.append((day, temp, humidity))
    return weather

def display_weather(weather):
    print("Day | Temp (°C) | Humidity (%)")
    print("-"*30)
    for day, temp, hum in weather:
        print(f"{day:3} | {temp:8} | {hum:11}")

if __name__ == "__main__":
    data = generate_weather_data()
    display_weather(data)
