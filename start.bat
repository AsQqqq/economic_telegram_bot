@echo off
setlocal enableextensions enabledelayedexpansion

echo Hello! You were met by the launch system version 0.1
echo

:Repeat

echo select to:
echo.
echo 1. Start BOT
echo 2. Start VENV
echo 3. Start CMD
echo 4. Create VENV and install libraries
echo 5. only Installing Libraries
echo ================
echo 6. exit
echo.
choice /c 123456 /m "input: "

call :Choice%ErrorLevel%
goto :Repeat

endlocal
exit /b 0

:Choice1
    start BAT\startbot.bat
    exit

:Choice2
    start venv\Scripts\activate.bat
    exit

:Choice3
    cls
    cmd

:Choice4
    start BAT\create_install.bat
    exit

:Choice5
    start BAT\install.bat
    exit

:Choice6
    exit

:Choice0
    rem Nothing to do
    exit /b 0