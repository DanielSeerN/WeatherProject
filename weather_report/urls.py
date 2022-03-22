from django.urls import path

from .views import (show_main_page,
                    search_city,
                    current_weather_report_page,
                    weather_for_7days_page
                    )


urlpatterns = [
    path('', show_main_page),
    path('search/', search_city),
    path('forecast-current/<str:city>', current_weather_report_page),
    path('forecast-7days/<str:city>', weather_for_7days_page),

]