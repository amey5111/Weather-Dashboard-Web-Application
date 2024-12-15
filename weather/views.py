import requests
from django.shortcuts import render

# Replace with your API keys
WEATHER_API_KEY = '45eceb921295ee4d822aa508b3185d0e'
NEWS_API_KEY = 'a66853700bb84f3bb0133ed5fb8d9823'

def dashboard(request):
    city = request.GET.get('city', 'London')  # Default to London if no city is searched
    weather_data = fetch_weather_data(city)
    forecast_data = fetch_forecast_data(city)
    news_data = fetch_weather_news()

    context = {
        'weather': weather_data,
        'forecast': forecast_data,
        'news': news_data,
        'city': city,
        "weather_api_key": "45eceb921295ee4d822aa508b3185d0e",
        "google_maps_api_key": "AIzaSyAxVAdBiQtgyFYDoKdqXeXL_9kq5H2Oc4w",
    }
    return render(request, 'dashboard.html', context)

def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()
    return response

def fetch_forecast_data(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()
    return response

def fetch_weather_news():
    url = f"https://newsapi.org/v2/everything?q=weather&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    return response['articles'][:5]
