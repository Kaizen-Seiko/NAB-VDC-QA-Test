"""
Test environment config
"""
from core.abstract.PageFactory import *
from core.abstract.BaseTest import *

# Project folder hierarchy
DIR_ROOT = os.path.realpath(os.getcwd())
DIR_TEMP = f'{DIR_ROOT}\\temp'
DIR_SOURCES = f'{DIR_ROOT}\\sources'
DIR_REPORTS = f'{DIR_ROOT}\\reports'
DIR_WEBDRIVERS = DIR_SOURCES


# Webdriver
OW_PF = PageFactory('OpenWeather')
OW_PF.storeEnvironment('UAT', Environment('UAT', 'https://openweathermap.org'))