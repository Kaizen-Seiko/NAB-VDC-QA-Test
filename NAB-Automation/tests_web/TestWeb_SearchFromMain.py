import allure
import pytest
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pom.environment import *

# Data driven
scenarios = [Scenario.gen('Few results', ('Hanoi', 1)),
             Scenario.gen('Dozen results', ('London', 2)),
             Scenario.gen('No results', ('Koala', 3)),
             ]


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
            assert self.driver.is_visible(OW_PF.pageMain.txtSearch, self.timeout / 2), \
                'Could not detect search box on top menu'

    @allure.severity(allure.severity_level.CRITICAL)
    def test_web_tc002_search_mainpage(self):
        with allure.step(f'GIVEN Guest is on Main Page'):
            OW_PF.pageMain.go()
        with allure.step(f'WHEN He input a valid city name into search box'):
            self.driver.is_visible(OW_PF.pageMain.txtSearch, self.timeout / 2)
            self.driver.input_text(OW_PF.pageMain.txtSearch, 'Hanoi')
        with allure.step(f'AND He clicks on submit button'):
            self.driver.click(OW_PF.pageMain.btnSubmit)
        with allure.step(f'THEN Search result page is navigated'):
            assert self.driver.is_visible(OW_PF.pageWeatherInYourCity.imgTitle, self.timeout / 2), \
                'Failed to detect search result page after submit'

    @pytest.mark.parametrize('keyword, results', *Scenario.parse(scenarios, False))
    @allure.severity(allure.severity_level.CRITICAL)
    def test_web_tc003_search_mainpage(self, keyword, results):
        with allure.step(f'GIVEN Guest is on Main Page'):
            OW_PF.pageMain.go()
        with allure.step(f'WHEN He inputs a valid city name into search box'):
            self.driver.is_visible(OW_PF.pageMain.txtSearch, self.timeout / 2)
            self.driver.input_text(OW_PF.pageMain.txtSearch, keyword)
        with allure.step(f'AND He presses Enter'):
            self.driver.send_keys(OW_PF.pageMain.txtSearch, Keys.ENTER)
        with allure.step(f'THEN Search result page is navigated'):
            assert self.driver.is_visible(OW_PF.pageWeatherInYourCity.imgTitle, self.timeout / 2), \
                'Failed to detect search result page after submit'
        with allure.step(f'AND Keyword retains in result search box'):
            assert keyword in self.driver.get_value(OW_PF.pageWeatherInYourCity.txtSearch), \
                'Searched keyword does not retain in search box'

        items = self.driver.find_all((By.CSS_SELECTOR, f"{OW_PF.pageWeatherInYourCity.tblResult[1]} tr"))
        for item in items:
            with allure.step(f'AND Weather icon, City name, Country flag, Weather description show on first line'):
                source = self.driver.get_inner_html(item)
                childs = BeautifulSoup(source, 'html.parser')
                assert childs.select('td:nth-child(1)>img')[0].has_attr('src')
                assert childs.select('td:nth-child(1)>img')[0].get('width') == '50'
                assert childs.select('td:nth-child(1)>img')[0].get('height') == '50'
                assert childs.select('td:nth-child(2)>b>a')[0].has_attr('href')
                assert childs.select('td:nth-child(2)>img')[0].has_attr('src')
            with allure.step(f'AND Temp, Temp Min, Temp Max, Wind, Cloud, Pressure show on second line'):
                assert childs.select('td:nth-child(2)>p>span')[0].get('class') == ['badge', 'badge-info']
                assert 'temperature from' in childs.select('td:nth-child(2)>p')[0].text.strip()
            with allure.step(f'AND Geo coords show on third line'):
                assert 'Geo coords' in childs.select('td:nth-child(2)>p:last-child')[0].text
        with allure.step(f'AND Browser does not get any error return'):
            for log in self.driver.get_log('browser'):
                assert log['level'] != 'SEVERE', 'Found error in browser console: %s' % log['message']
