from django.urls import path

from .views import (main_page,
                    get_weather_for_today,
                    current_weather_report_page,
                    get_weather_for_7days,
                    weather_for_7days_page
                    )


urlpatterns = [
    path('', main_page),
    path('search-current/', get_weather_for_today),
    path('search-7days/', get_weather_for_7days),
    path('forecast-current/<str:city>', current_weather_report_page),
    path('forecast-7days/<str:city>', weather_for_7days_page),

]