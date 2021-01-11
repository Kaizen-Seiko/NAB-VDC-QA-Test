import allure
import pytest
from pom.environment import *


@allure.feature('#1 - [OpenWeather] Weather in your city')
@allure.story('As a GUEST, I want to be able to search for weather forecast from search box on main page')
@pytest.mark.usefixtures('init_environment', 'launch')
class TestWeb_SearchFromMain(BaseUITest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_web_search_from_main(self):
        with allure.step(f'Open main page'):
            OW_PF.pageMain.go()
