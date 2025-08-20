n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Forecast():
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

rain_forecasts = [Forecast(date[i], day[i], weather[i]) 
                for i in range(n)
                if weather[i] == "Rain"]

first_rain_forecast = sorted(rain_forecasts, key=lambda f: f.date)[0]

print(first_rain_forecast.date,first_rain_forecast.day,first_rain_forecast.weather)

    


