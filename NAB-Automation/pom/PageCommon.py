from selenium.webdriver.common.by import By
from core.abstract.PageFactory import Page


class PageCommon(Page):
    """
        Web Interface for test runs
        Parent class: PageFactory.Page
    """
    # Controls #
    imgLogo = (By.XPATH, "//*[@id='header-website']/*[@class='logo']/a/img")

    # Private #
    def __init__(self, driver):
        super(PageCommon, self).__init__(driver)
