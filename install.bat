@echo off

cls





echo installation may take from 1 to 5 minutes. A virtual environment for the bot will be created and all libraries will be installed.

set /p YN="Continue?(y/n) "
if /i "%YN%"=="Y" (echo Great timeout 1) else (exit)

if not exist venv (
    cls
    echo Wait for the download...
    python -m venv venv
    cls
    echo venv has been created
    timeout 2
    cls
)


echo @echo off >> pre_install.bat
echo call venv\Scripts\activate.bat >> pre_install.bat
echo python -m pip install --upgrade pip >> pre_install.bat
echo pip install -r requirements.txt >> pre_install.bat
echo cls >> pre_install.bat
echo echo the files have been installed and created, run through the start.bat file >> pre_install.bat
echo timeout 15 >> pre_install.bat
echo cls >> pre_install.bat
echo echo thanks for installing >> pre_install.bat
echo del requirements.txt >> pre_install.bat
echo exit >> pre_install.bat

start pre_install.bat

echo %echo off > start.bat
echo if exist pre_install.bat (del pre_install.bat) >> start.bat
echo call venv\Scripts\activate.bat >> start.bat
echo python app.py >> start.bat
echo pause >> start.bat

if not exist config.py (
    echo ADMINS=1234567(ADMIN_ID) > config.py
    echo TOKEN="AaBbCcDd:1A2B3C4D"(TOKEN) >> config.py
)

del install.bat || exit