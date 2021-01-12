@echo OFF
cls
if not exist "%~dp0\temp" mkdir "%~dp0\temp"

:: RUN TESTS
set PYTHONDONTWRITEBYTECODE=1
set PYTHONUNBUFFERED=1
cmd /c pytest -v --tb=line --browser firefox --domain uat -m web --alluredir "%~dp0\reports"
pause