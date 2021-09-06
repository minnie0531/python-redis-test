@echo off

:: This script to configure virtual envrivonmnet on Windows

SET OS = "%get-wmiobject -class win32_operatingsystem%"
echo %OS% 

echo "Set up vitual evironment for windows"
SET CURRENTDIR="%cd%"
echo %CURRENTDIR%
cmd /k  "python -m venv venv & cd /d venv/Scripts & activate & cd /d ../.. & pip install -r requirements.txt"
echo "Move pre-commit to .git/hooks"
copy %CURRENTDIR%\hooks\pre-commit.py %CURRENTDIR%\.git\hooks\pre-commit /y /s /e
