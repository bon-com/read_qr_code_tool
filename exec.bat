@echo off

powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope Process -Force"
call .\myenv\Scripts\activate.bat

REM Pythonスクリプト実行
python read_qr_code.py

pause
