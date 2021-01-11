import allure
import pytest
from pom.environment import *

# Test variables


@allure.feature('#132623 - [CTS] Implement Customer Category')
@allure.story('As a member of Fraud Team, I want to manage customer with Categories in CTS')
@pytest.mark.usefixtures('init_environment', 'cts_launch', 'cts_login')
class TestWeb_SearchFromMain(BaseUITest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_web_search_from_main(self):
        with allure.step(f'Open profile page of ctsCustID'):
            OW_PF.pageMain.go()
