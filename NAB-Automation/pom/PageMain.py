from selenium.webdriver.common.by import By
from pom.PageCommon import PageCommon


class PageMain(PageCommon):
    """
        Web Interface for test runs
        Parent class: PageCommon.PageCommon
    """
    # Statistic #
    url = ''

    # Controls #
    imgTitle = (By.XPATH, "//*[@class='orange-text' and normalize-space(text())='OpenWeather']")
    txtSearch = (By.XPATH, "//form[@id='nav-search-form']/*[@placeholder='Weather in your city']")

    # Private #
    def __init__(self, driver):
        super(PageMain, self).__init__(driver)

    # Public #
    def go(self):
        super(PageMain, self).go(self.url)
        return self
