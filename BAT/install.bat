@echo off

echo preparation before installation
timeout 3
cls

python -m pip install --upgrade pip
pip install -r requirements.txt
timeout 1

cls
echo install complited
timeout 2

start ..\calculate_salaries\start.bat
exit