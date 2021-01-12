import allure
import pytest
import requests
import json
from pom.environment import *

# Data driven
tc012_scenarios = load_resource(f'{DIR_DATA}/tc012_scenarios.xlsx', 'Sheet1')


def url(domain, q, type, sort, cnt, appid):
    uri = '/data/2.5/find'
    param_q = f'&q={q}' if q is not None else ''
    param_type = f'&type={type}' if type is not None else ''
    param_sort = f'&sort={sort}' if sort is not None else ''
    param_cnt = f'&cnt={cnt}' if cnt is not None else ''
    param_appid = f'&appid={appid}' if appid is not None else ''
    return f'{domain}/{uri}?{param_q}{param_type}{param_sort}{param_cnt}{param_appid}'


def headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.61 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'Accept': 'application/json,text/json,text/html,application/xhtml+xml,application/xml;q=0.9'
                  ',image/webp,image/apng,*/*;q=0.8, application/signed-exchange;v=b3;q=0.9'
    }


@allure.feature('#1 - [OpenWeather] Weather in your city')
@allure.story('As a GUEST, I want to be able to send http request to get weather information')
@pytest.mark.usefixtures('init_environment')
class TestAPI_SearchWeather(BaseAPITest):

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize('q, type, sort, cnt, appid, result', *Scenario.parse(tc012_scenarios, False))
    def test_api_tc012_search_weather(self, q, type, sort, cnt, appid, result):
        with allure.step(f'GIVEN Using API injection tool'):
            session = requests.Session()
        with allure.step(f'WHEN User sends GET to /data/2.5/find'
                         f'AND q={q}'
                         f'AND appid={appid}'):
            response = session.get(url=url(self.environment.domain, q, type, sort, cnt, appid),
                                   headers=headers())
        with allure.step(f'THEN Status 200'):
            assert response.status_code == 200, 'Status code is not as expected'
        with allure.step(f'AND Body as Json matches expected dataset'):
            assert response.text == result

    @allure.severity(allure.severity_level.CRITICAL)
    def test_api_tc013_search_weather(self):
        with allure.step(f'GIVEN Using API injection tool'):
            session = requests.Session()
        with allure.step(f'WHEN User sends GET to /data/2.5/find'
                         f'AND missing q'):
            response = session.get(url=url(self.environment.domain, None, 'like', 'population', '30', DEFAULT_APPID),
                                   headers=headers())
        with allure.step(f'THEN Status 500 '):
            assert response.status_code == 500, 'Status code is not as expected'
        with allure.step('AND Message "{"cod": 500,"message": "Internal server error"}'):
            assert response.text == '{"cod": 500,"message": "Internal server error"}' \
                , 'Response body is not as expected'

    @allure.severity(allure.severity_level.CRITICAL)
    def test_api_tc014_search_weather(self):
        with allure.step(f'GIVEN Using API injection tool'):
            session = requests.Session()
        with allure.step(f'WHEN User sends GET to /data/2.5/find '
                         f'AND q=Hanoi'
                         f'AND missing appid'):
            response = session.get(url=url(self.environment.domain, 'Hanoi', 'like', 'population', '30', None),
                                   headers=headers())
        with allure.step(f'THEN Status 401 '):
            assert response.status_code == 401, 'Status code is not as expected'
        with allure.step('AND Message {"cod": 401,"message": "Invalid API key. Please see '
                         'http://openweathermap.org/faq#error401 for more info."}'):
            assert response.text == '{"cod": 401,"message": "Invalid API key. Please see ' \
                                    'http://openweathermap.org/faq#error401 for more info."}' \
                , 'Response body is not as expected'

    @allure.severity(allure.severity_level.NORMAL)
    def test_api_tc015_search_weather(self):
        with allure.step(f'GIVEN Using API injection tool'):
            session = requests.Session()
        with allure.step(f'WHEN User sends GET to /data/2.5/find '
                         f'AND q=Hanoi '
                         f'AND appid=439d4b804bc8187953eb36d2a8c26a02 '
                         f'AND missing type'):
            response = session.get(url=url(self.environment.domain, 'Hanoi', None, 'population', '30', DEFAULT_APPID),
                                   headers=headers())
        with allure.step(f'THEN Status 200 '):
            assert response.status_code == 200, 'Status code is not as expected'
        with allure.step('AND AND Body as Json matches expected dataset'):
            result = json.loads(f'{response.text}'.replace('\'', '\"'))
            # Verify first item
            assert result['list'][0]['id'] == 1581130
            assert result['list'][0]['name'] == 'Ha Noi'
            assert result['list'][0]['coord'] == {'lat': 21.0245, 'lon': 105.8412}
            #assert result['list'][0]['dt'] == 1610446167
            #assert result['list'][0]['wind'] == {'speed': 2.06, 'deg': 300}
            assert result['list'][0]['sys'] == {'country': 'VN'}
            assert result['list'][0]['rain'] is None
            assert result['list'][0]['snow'] is None
            #assert result['list'][0]['clouds'] == {'all': 0}
            #assert result['list'][0]['weather'] == [{'id': 800,
            #                                         'main': 'Clear',
            #                                         'description': 'clear sky',
            #                                         'icon': '01d'}]
            #assert result['list'][0]['main'] == {'temp': 291.15, 'feels_like': 287,
            #                                     'temp_min': 291.15,
            #                                     'temp_max': 291.15,
            #                                     'pressure': 1022,
            #                                     'humidity': 19}

            # Verify second item
            assert result['list'][1]['id'] == 1581129
            assert result['list'][1]['name'] == 'Thủ Ðô Hà Nội'
            assert result['list'][1]['coord'] == {'lat': 21.1167, 'lon': 105.8833}
            #assert result['list'][1]['dt'] == 1610445941
            #assert result['list'][1]['wind'] == {'speed': 2.06, 'deg': 300}
            assert result['list'][1]['sys'] == {'country': 'VN'}
            assert result['list'][1]['rain'] is None
            assert result['list'][1]['snow'] is None
            #assert result['list'][1]['clouds'] == {'all': 0}
            #assert result['list'][1]['weather'] == [{'id': 800,
            #                                         'main': 'Clear',
            #                                         'description': 'clear sky',
            #                                         'icon': '01d'}]
            #assert result['list'][1]['main'] == {'temp': 291.15,
            #                                     'feels_like': 287,
            #                                     'temp_min': 291.15,
            #                                     'temp_max': 291.15,
            #                                     'pressure': 1022,
            #                                     'humidity': 19}
