import allure
import pytest
from selenium.webdriver.common.keys import Keys
from pom.environment import *


@allure.feature('#1 - [OpenWeather] Weather in your city')
@allure.story('As a GUEST, I want to be able to search for weather forecast from search box on main page')
@pytest.mark.usefixtures('init_environment', 'launch')
class TestWeb_SearchFromMain(BaseUITest):
    @allure.severity(allure.severity_level.BLOCKER)
    def test_web_tc001_search_mainpage(self):
        with allure.step(f'GIVEN Guest is on Main Page'):
            OW_PF.pageMain.go()
        with allure.step(f'WHEN He looks at the top menu'):
            pass
        with allure.step(f'THEN He sees weather search box on top menu next to the logo'):
            assert self.driver.is_visible(OW_PF.pageMain.txtSearch, self.timeout/2),\
                'Could not detect search box on top menu'

    @allure.severity(allure.severity_level.CRITICAL)
    def test_web_tc002_search_mainpage(self):
        with allure.step(f'GIVEN Guest is on Main Page'):
            OW_PF.pageMain.go()
        with allure.step(f'WHEN He input a valid city name into search box'):
            self.driver.is_visible(OW_PF.pageMain.txtSearch, self.timeout/2)
            self.driver.input_text(OW_PF.pageMain.txtSearch, 'Hanoi')
        with allure.step(f'AND He clicks on submit button'):
            self.driver.click(OW_PF.pageMain.btnSubmit)
        with allure.step(f'THEN Search result page is navigated'):
            assert self.driver.is_visible(OW_PF.pageWeatherInYourCity.imgTitle, self.timeout/2),\
                'Failed to detect search result page after submit'

    @allure.severity(allure.severity_level.CRITICAL)
    def test_web_tc003_search_mainpage(self):
        with allure.step(f'GIVEN Guest is on Main Page'):
            OW_PF.pageMain.go()
        with allure.step(f'WHEN He input a valid city name into search box'):
            self.driver.is_visible(OW_PF.pageMain.txtSearch, self.timeout/2)
            self.driver.input_text(OW_PF.pageMain.txtSearch, 'Hanoi')
        with allure.step(f'AND He press Enter'):
            self.driver.send_keys(OW_PF.pageMain.txtSearch, Keys.ENTER)
        with allure.step(f'THEN Search result page is navigated'):
            assert self.driver.is_visible(OW_PF.pageWeatherInYourCity.imgTitle, self.timeout/2),\
                'Failed to detect search result page after submit'
        with allure.step(f'AND Keyword retains in result search box'):
            assert 'Hanoi' in self.driver.get_value(OW_PF.pageWeatherInYourCity.txtSearch),\
                'Searched keyword does not retain in search box'
