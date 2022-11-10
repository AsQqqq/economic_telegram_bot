@echo off

echo preparation before installation
timeout 3
cls

python -m pip install --upgrade pip
python -m venv venv
pip install -r requirements.txt
timeout 1

cls
echo create and install complited
timeout 2

start ..\calculate_salaries\start.bat
exit