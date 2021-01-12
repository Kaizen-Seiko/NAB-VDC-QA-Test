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
DIR_DATA = f'{DIR_ROOT}\\data'
DIR_WEBDRIVERS = DIR_SOURCES

# Resources
DEFAULT_APPID = '439d4b804bc8187953eb36d2a8c26a02'

# Webdriver
OW_PF = PageFactory('OpenWeather')
OW_PF.storeEnvironment('UAT', Environment('UAT', 'https://openweathermap.org'))
