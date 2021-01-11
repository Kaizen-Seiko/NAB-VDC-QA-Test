@echo OFF
:: CLEAN UP PREVIOUS REPORTS
echo:
echo #### Clean up junk files
del /f /q /s "%~dp0\test.log"
del /f /q /s "%~dp0\reports\*.*"
rmdir /q /s "%~dp0\reports\"
del /f /q /s "%~dp0\temp\*.*"
rmdir /q /s "%~dp0\temp\"
if not exist "%~dp0\temp" mkdir "%~dp0\temp"
if not exist "%~dp0\reports" mkdir "%~dp0\reports"