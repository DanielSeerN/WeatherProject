from django.test import TestCase, RequestFactory
from .views import show_main_page, search_city, weather_for_7days_page, current_weather_report_page


class AppTest(TestCase):
    """
    Тесты приложения
    """

    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_response_from_main_page(self):
        """
        Тест ответа от представления для главной страницы
        """
        request = self.factory.get('')
        response = show_main_page(request)
        self.assertEqual(response.status_code, 200)

    # def test_search_for_city(self):
    #     request = self.factory.get('')
    #     response = search_city(request)

    def test_response_from_weather_for_7days(self):
        """
        Тест ответа от представления для прогноза на 7 дней
        """
        request = self.factory.get('')
        response = weather_for_7days_page(request, city='london')
        self.assertEqual(response.status_code, 200)

    def test_response_from_current_weather_report(self):
        """
        Тест ответа от представления для прогноза сейчас
        """
        request = self.factory.get('')
        response = current_weather_report_page(request, city='london')
        self.assertEqual(response.status_code, 200)


# Create your tests here.
