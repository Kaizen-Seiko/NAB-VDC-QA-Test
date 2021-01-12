@echo OFF
if not exist "%~dp0\temp" mkdir "%~dp0\temp"

:: RUN TESTS
set PYTHONDONTWRITEBYTECODE=1
set PYTHONUNBUFFERED=1
cmd /c pytest -v --tb=line --browser chrome --domain uat -m api --alluredir "%~dp0\reports"