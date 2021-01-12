from selenium.webdriver.common.by import By
from pom.PageCommon import PageCommon


class PageWeatherInYourCity(PageCommon):
    """
        Web Interface for test runs
        Parent class: PageCommon.PageCommon
    """
    # Statistic #
    url = 'find?q='

    # Controls #
    imgTitle = (By.XPATH, "//h2[normalize-space(text())='Weather in your city']")
    txtSearch = (By.CSS_SELECTOR, "input#search_str")
    btnSubmit = (By.CSS_SELECTOR, "button[type=submit]")

    tblResult = (By.CSS_SELECTOR, "#forecast_list_ul>table")

    # Private #
    def __init__(self, driver):
        super(PageWeatherInYourCity, self).__init__(driver)

    # Public #
    def go(self, keyword=''):
        super(PageWeatherInYourCity, self).go('%s/%s' % (self.url, keyword))
        self.driver.is_visible(self.imgTitle, self.timeout)
        return self
