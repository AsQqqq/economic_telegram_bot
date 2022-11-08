@echo off
setlocal enableextensions enabledelayedexpansion

:Repeat

echo select to:
echo.
echo 1. Start BOT
echo 2. Start VENV
echo ================
echo 3. exit
echo.
choice /c 123 /m "input: "

call :Choice%ErrorLevel%
goto :Repeat

endlocal
exit /b 0

:Choice1
	start startbot.bat
	exit

:Choice2
    start venv\Scripts\activate.bat
	exit

:Choice3
	exit

:Choice0
	rem Nothing to do
	exit /b 0