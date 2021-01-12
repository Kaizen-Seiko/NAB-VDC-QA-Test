# NAB-VDC-QA-Test
QA Development Challenge for NAB VDC
Owner: Thong.Khuat

Delivery package:
	- Readme.md (Package structure & project description)
	- Installation Guide
	- python-3.8.2.exe (python installation source)
	
	Manual test:
		- P1.1 - Test Approach.docx
		- P1.1 - Test Charter.docx
		- P1.2 - Testcases.xlsx
		- P1.3 - Bug Report.xlsx
	
	Automation test:
		+ NAB-Automation
			- allure.zip
			- batch_rpt_build.bat
			- batch_rpt_cleanup.bat
			- batch_run_api.bat
			- batch_run_web.bat
			- conftest.py
			- pytest.ini
			+ core
				+ abstract
					- BaseFactory.py
					- BaseTest.py
					- PageFactory.py
				+ libs
					- Loop.py
					- WebDriver.py
			+ data
				- tc012_scenarios.xlsx
			+ pom
				- environment.py
				- PageCommon.py
				- PageMain.py
				- PageWeatherInYourCity.py
			+ reports
			+ temp
			+ sources
				- chromedriver.exe
				- geckodriver.exe
			+ tests_api
				- TestAPI_SearchCity.py
			+ tests_web
				- TestWeb_SearchFromMain.py