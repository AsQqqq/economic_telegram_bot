@echo off
setlocal enableextensions enabledelayedexpansion

:Repeat

echo Is Python installed?(y,n):
choice /c yn /m "input: "

call :Choice%ErrorLevel%
goto :Repeat

endlocal
exit /b 0

:Choice1
	start BAT\create.bat
	exit

:Choice2
    start ..\calculate_salaries\start.bat
	exit

:Choice0
	rem Nothing to do
	exit /b 0