from django.shortcuts import render, redirect

from services.forecast_services import get_7days_weather_data, get_current_weather_data
from services.geolocation_services import get_location


def show_main_page(request):
    return render(request, 'weather_rep/index.html')


def search_city(request):
    city = str(request.POST.get('city_today'))
    return redirect(f'/forecast-current/{city}')


def weather_for_7days_page(request, **kwargs):
    city = kwargs.get('city')
    context = {
        'forecasts': get_7days_weather_data(get_location(city))
    }
    return render(request, 'weather_rep/7days_weather.html', context)


def current_weather_report_page(request, **kwargs):
    city = kwargs.get('city')
    return render(request, 'weather_rep/current_weather.html', get_current_weather_data(city))
# Create your views here.
